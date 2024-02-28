document.addEventListener("DOMContentLoaded",function(){
    document.getElementById('')
    function hover(){
        document.getElementById('navbar-cloth').addEventListener('mouseover', function () {
            document.getElementById('Link2').style.backgroundColor = '#880500';
            document.getElementById('Link2').style.fontSize = '4.5em';
        });

        document.getElementById('navbar-cloth').addEventListener('mouseout', function () {
            document.getElementById('Link2').style.backgroundColor = '';
            document.getElementById('Link2').style.fontSize = '';
        });
        document.getElementById('navbar-food').addEventListener('mouseover', function () {
            document.getElementById('Link3').style.backgroundColor = '#880500';
            document.getElementById('Link3').style.fontSize = '4.5em';
        });

        document.getElementById('navbar-food').addEventListener('mouseout', function () {
            document.getElementById('Link3').style.backgroundColor = '';
            document.getElementById('Link3').style.fontSize = '';
        });
        document.getElementById('navbar-elec').addEventListener('mouseover', function () {
            document.getElementById('Link1').style.backgroundColor = '#880500';
            document.getElementById('Link1').style.fontSize = '4.5em';
        });

        document.getElementById('navbar-elec').addEventListener('mouseout', function () {
            document.getElementById('Link1').style.backgroundColor = '';
            document.getElementById('Link1').style.fontSize = '';
        });
    }
    hover()
})