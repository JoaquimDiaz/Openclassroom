from branca.element import Template, MacroElement  *
# Macro pour la legende
template = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>jQuery UI Draggable - Default functionality</title>
<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

<script>
$( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

</script>
</head>
<body>


<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255,255, 255, 0.8);
    border-radius:6px; padding: 10px; font-size:14px; right: 0px; bottom: 0px;'>
    
<div class='legend-title'>Type de milieu</div>
<div class='legend-scale'>
<ul class='legend-labels'>
    <li><span style='background:lightblue;opacity:0.7;'></span>Littoral (terrestre)</li>
    <li><span style='background:darkblue;opacity:0.7;'></span>Mer - Océan</li>
    <li><span style='background:cyan;opacity:0.7;'></span>Cours d'eau</li>
    <li><span style='background:green;opacity:0.7;'></span>Zone naturelle ou rurale (hors littoral et montagne)</li>
    <li><span style='background:orange;opacity:0.7;'></span>Zone urbaine</li>
    <li><span style='background:red;opacity:0.7;'></span>Lagune et étang côtier</li>
    <li><span style='background:pink;opacity:0.7;'></span>Multi-lieux</li>
    <li><span style='background:grey;opacity:0.7;'></span>Montagne</li>
    <li><span style='background:black;opacity:0.7;'></span>Présent au sol (abandonné)</li>

</ul>
</div>
</div>

</body>
</html>

<style type='text/css'>
.maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
.maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
.maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
.maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
.maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
.maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

macro = MacroElement()
macro._template = Template(template)

m.get_root().add_child(macro)