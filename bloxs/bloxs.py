

class B:

    def __init__(self, data, title = "", description="", percent_change = None, points = None):
        self.data = data
        self.title = title
        self.blox_type = 'numeric'
        if isinstance(self.data, list):
          self.blox_type = 'list' 
        self.percent_change = percent_change
        

    def _repr_html_(self):
        if self.blox_type == "list":
            bloxs = ""
            for b in self.data:
                if isinstance(b, B):
                    bloxs += b._repr_html_()

            return f"""<div style="display: flex; background: #fff">{bloxs}</div>"""
            
        percent_change_html = ""
        if self.percent_change is not None:
            if self.percent_change > 0:
                percent_change_html = f"""
                <span style="font-size: 0.3em; color: green; font-family: monospace;"> + {self.percent_change}%</span>
                """
            else:
                percent_change_html = f"""
                <span style="font-size: 0.3em; color: red; font-family: monospace;"> {self.percent_change}%</span>
                """
  

        return f"""
<div style="text-align: center; width: 30%; border: 1px solid #e5e5e5; margin: 10px; padding-top: 40px; padding-bottom: 40px; background: white; border-radius:5px">
  <span style="font-size: 4em; color: #5a5a5a; font-family: monospace; ">{self.data:,}{percent_change_html}</span>
  <span style="font-size: 2em; color: gray; display: block; padding-top: 20px; font-family: monospace;">{self.title}</span>
</div>
  """