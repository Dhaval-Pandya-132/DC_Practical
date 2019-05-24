<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Googlemap.aspx.cs" Inherits="PoweroutageMap.Googlemap" %>

<style type="text/css">
html { height: 100% }
body { height: 100%; margin: 0; padding: 0 }
#map_canvas { height: 100% }
</style>

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js" type="text/javascript"></script>

<script type="text/javascript" src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyAkDmO3sVWTn5w7I5-dtmM11uii4VgF7uM&sensor=false">
</script>

<script type = "text/javascript">

    $(document).ready(function () {
        //alert('Alert message ');
        //ShowCurrentTime();
    });


    function ShowCurrentTime() {
        debugger;
    $.ajax({
        type: "POST",
        url: "Googlemap.aspx/GetCurrentTime",
        data: '{name: "Dhaval" }',
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: OnSuccess,
        failure: function(response) {
            alert(response.d);
        }
    });
}
function OnSuccess(response) {
    alert(response.d);
    }


    function initialize() {
        var markers = JSON.parse('<%=CreateConnection() %>');
        var mapOptions = {
            center: new google.maps.LatLng(markers[0].Lat, markers[0].Long),
            zoom: 5,
            mapTypeId: google.maps.MapTypeId.ROADMAP
            //  marker:true
        };
        var infoWindow = new google.maps.InfoWindow();
        var map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
        for (i = 0; i < markers.length; i++) {
            var data = markers[i]
            console.log(data);
            
            var myLatlng = new google.maps.LatLng(data.Lat, data.Long);
            var marker = new google.maps.Marker({
                position: myLatlng,
                map: map,
                city: data.city
            });
            (function (marker, data) {
                var dateValue = parseInt(data.StartDate.replace(/\/Date\((\d+)\)\//g, "$1"));
                data.StartDate = new Date(dateValue);

                if (data.ETR != null) {
                    var dateValue2 = parseInt(data.ETR.replace(/\/Date\((\d+)\)\//g, "$1"));
                    data.ETR = new Date(dateValue2);}
                else { data.ETR = ""; }
                
                if (data.Cause == null) {
                    data.Cause = "";
                }
                var datastring = '<b>Affected Customer :<b/> ' + data.Affected_Customer + ' <br/>';
                datastring = datastring + '<b>Lat:<b/> ' + data.Lat + ' <br/>';
                datastring = datastring + '<b>Long:<b/> ' + data.Long + ' <br/>';
                datastring = datastring + '<b>StartDate :<b/> ' + data.StartDate + ' <br/>';
                datastring = datastring + '<b>ETR:<b/> ' + data.ETR + ' <br/>';
                datastring = datastring + '<b>Cause :<b/> ' + data.Cause + ' <br/>';
                // Attaching a click event to the current marker
                google.maps.event.addListener(marker, "click", function (e) {
                    infoWindow.setContent(datastring);
                    infoWindow.open(map, marker);
                });
            })(marker, data);
        }
    }


</script>
<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body  onload="initialize()">
    <form id="form1" runat="server">
        <div id="map_canvas" style="width: 800px; height: 800px"></div>
    </form>
</body>
</html>
