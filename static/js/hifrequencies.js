$(document).ready(function() {
    $(document).on('click', '#soundcloud-button', function() {
        function getRandomInt(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }
        urlpost = getRandomInt(0, 99)
        $.ajax({
            type:"GET",
            url: "/ajax/random-song/" + urlpost,
            success: function(data) {
                document.getElementById('soundcloud_player').innerHTML = data
            }
        });
    });

    $(document).on('click', '#load-news', function() {
        $.ajax({
            type:"GET",
            url: "/ajax/load-news/",
            success: function(data) {
                document.getElementById('news-group').innerHTML += data
            }
        });
    });

    $(document).on('click', '#less', function() {
        $.ajax({
            type:"GET",
            url: "/ajax/less-news/",
            success: function(data) {
                document.getElementById('news-group').innerHTML = data
            }
        });
    });
});