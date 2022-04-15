$(document).each(function () {
    const div = document.querySelector('.progress_bar');
    // var ex = Number(document.getElementById("exdate").textContent);
    // var pr = Number(document.getElementById("prdate").textContent);
    var count = Number (document.querySelector('.count').textContent);
    var ex = Number (document.querySelector('.exdate').textContent);
    var pr = Number( document.querySelector('.prdate').textContent);
    //var dateObj = new Date(x);
    //var pr = document.getElementById("prdate").textContent;
    console.log(count);
    console.log(ex);
    console.log(pr);
    var now = new Date().getFullYear();
    // console.log(now);
    // var remain = ex - now;
    // console.log(remain);

    var countDownDate = new Date("Jan 5, 2019 15:37:25").getTime();
    var startDate = new Date("Dec 1, 2018, 10:00:00").getTime();
// Update the count down every 1 second
// Get todays date and time
    // var now = new Date().getTime();

// Find the distance between now and the count down date
    // var distanceWhole = countDownDate - startDate;
    // var distanceLeft = countDownDate - now;
    var distanceWhole = ex - pr;
    var distanceLeft = ex - now;

// Time calculations for minutes and percentage progressed
    var minutesLeft = Math.floor(distanceLeft / (1000 * 60));
    var minutesTotal = Math.floor(distanceWhole / (1000 * 60));
    var progress = Math.floor(((distanceWhole - distanceLeft) / distanceWhole) * 100);
    console.log( progress)
    if (progress <=50) {
        //$(progressBars[i]).addClass("bg-success");
        $("#progress-bar").addClass("bg-success");
        $('#progressbar').attr('aria-valuenow', progress).css('width', progress + "%").html(progress + "% Complete");
    }else if ((progress >=50) && (progress <=75))  {
        //$(progressBars[i]).addClass("bg-success");
        $("#progressbar"+count).addClass("bg-warning");
        $('#progressbar').attr('aria-valuenow', progress).css('width', progress + "%").html(progress + "% Complete");
    } else if ((progress >=75) && (progress <=100))  {
        //$(progressBars[i]).addClass("bg-success");
        $("#progressbar").addClass("bg-danger");
        $('#progressbar').attr('aria-valuenow', progress).css('width', progress + "%").html(progress + "% Complete");
    }
    //$('#progressbar').attr('aria-valuenow', progress).css('width', progress + "%").html(progress + "% Complete");
});