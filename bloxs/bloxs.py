import os

class B:

    BLUE = "#00B1E4"
    LIGHT_BLUE = "rgba(0, 177, 228, 0.5)"
    RED = "#FF6384"
    LIGHT_RED = "rgba(255, 99, 132, 0.5)"
    GREEN = "#00B275"
    LIGHT_GREEN = "rgb(0, 178, 117, 0.5)"

    def __init__(
        self,
        data,
        title="",
        percent_change=None,
        progress=None,
        color=None,
        points=None,
        chart_type=None,
    ):
        self.data = data
        self.title = title
        self.blox_type = "numeric"
        if isinstance(self.data, list):
            self.blox_type = "list"
        self.percent_change = percent_change
        self.progress = int(progress) if progress is not None else None
        self.color = color
        self.points = points
        self.chart_type = chart_type

        # position when displayed as a list
        self.position = None

    def _repr_html_(self):
        if self.blox_type == "list":
            bloxs = ""
            for i, b in enumerate(self.data):
                if isinstance(b, B):
                    b.position = i
                    bloxs += b._repr_html_()

            return f"""<div style="display: flex; background: #fff">{bloxs}</div>"""

        percent_change_html = ""
        if self.percent_change is not None:
            if self.percent_change > 0:
                percent_change_html = f"""
                <span style="font-size: 1.3em; color: {self.GREEN}; font-family: monospace;"> + {self.percent_change}%</span>
                """
            else:
                percent_change_html = f"""
                <span style="font-size: 1.3em; color: {self.RED}; font-family: monospace;"> {self.percent_change}%</span>
                """
        title_html = ""
        if self.title != "":
            title_html = f"""<span style="font-size: 2em; color: gray; display: block; padding-top: 20px; font-family: monospace; line-height: 1.3em;">{self.title}</span>"""

        progress_html = ""
        if self.progress is not None:
            color = self.BLUE
            if self.color is not None:
                if self.color == "red":
                    color = self.RED
                elif self.color == "blue":
                    color = self.BLUE
                elif self.color == "green":
                    color = self.GREEN
                else:
                    color = self.color

            progress_html = f"""
            <div style="background-color:#f1f1f1; margin: 10px">
                <div style="background-color:{color}; height:24px;width:{self.progress}%"></div>
            </div>
            """
        data_str = ""
        if isinstance(self.data, str):
            data_str = self.data
        else:
            data_str = f"{self.data:,}"

        script_html, chart_html = self.construct_chart_html()

        padding_bottom = "0px" if chart_html != "" else "40px"
        return f"""
<div style="text-align: center; width: 34%; border: 1px solid #e5e5e5; margin: 10px; padding-top: 40px; padding-bottom: {padding_bottom}; background: white; border-radius:5px">
  <span style="font-size: 4em; color: #5a5a5a; font-family: monospace; ">{data_str}</span>
  {percent_change_html}
  {title_html}
  {progress_html}
  {chart_html}
</div>

  {script_html}
  """

    def construct_chart_html(self):
        script_html, chart_html = "", ""

        if self.points is None:
            return script_html, chart_html

        title = (
            self.title
            if self.title is not None
            else f"chart-{len(self.points)}-{self.points[0]}"
        )

        position = self.position if self.position is not None else 0
        chartId = f"id-{title}-{position}"

        chart_html = (
            f"""<canvas id="{chartId}" style="width: 100%; border: 0px"></canvas>"""
        )

        border_color = self.BLUE
        fill_color = self.LIGHT_BLUE
        if self.color is not None:
            if self.color == "red":
                border_color = self.RED
                fill_color = self.LIGHT_RED
            elif self.color == "blue":
                border_color = self.BLUE
                fill_color = self.LIGHT_BLUE
            elif self.color == "green":
                border_color = self.GREEN
                fill_color = self.LIGHT_GREEN
            else:
                border_color = self.color

        points_str = ",".join([str(i) for i in self.points])

        stepped_html = ""
        if self.chart_type == "stepped":
            stepped_html = "stepped: 'middle',"

        script_html = ""
        if position == 0:
            script_html = f"""
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.1/chart.min.js" integrity="sha512-QSkVNOCYLtj73J4hbmVoOV6KVZuMluZlioC+trLpewV8qMjsWqlIQvkn1KGX2StWvPMdWGBqim1xlC8krl1EKQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
            
        """
        # need to figure out the way for offline serving ... ????
        # <script src="{self.path}/chart.3.7.1.min.js"></script>
        script_html += f"""
<script>
  const labels{position} = Array({len(self.points)}).fill('');

  const data{position} = {{
    labels: labels{position},
    datasets: [{{
      label: '{title}',
      backgroundColor: '{fill_color}',
      borderColor: '{border_color}',
      data: [{points_str}],
      fill: true,
      {stepped_html}
    }}]
  }};
  """
        script_html += f"""
  const config{position} = {{
    type: '"""
        script_html += "bar" if self.chart_type == "bar" else "line"
        script_html += f"""',
    data: data{position}"""
        script_html += """,
    options: { 
     elements: {
       point: {
         radius: 0,
       }
     },
     plugins: {
       legend: {
         display: false
       }
     },
     layout: {
       autoPadding: false
     },
     scales: {
       x: {
         display: false
       },
       y: {
         display: false
         """
        script_html += """
       }
     }
    },

  };
</script>
    """

        script_html += f"""

<script>
  const chart{position} = new Chart(
    document.getElementById('{chartId}'),
    config{position}
  );
</script>

        """

        return script_html, chart_html

    def path(self):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "js_dist")
