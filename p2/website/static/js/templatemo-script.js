const initBg = (autoplay = true) => {
    const bgImgsNames = ['diagoona-bg-1.jpg', 'diagoona-bg-2.jpg', 'diagoona-bg-3.jpg'];
    const bgImgs = bgImgsNames.map(img => "../static/img/" + img);

    $.backstretch(bgImgs, {duration: 4000, fade: 500});

    if(!autoplay) {
      $.backstretch('pause');  
    }    
}

const setBg = id => {
    $.backstretch('show', id);
}

const setBgOverlay = () => {
    const windowWidth = window.innerWidth;
    const bgHeight = $('body').height();
    const tmBgLeft = $('.tm-bg-left');

    $('.tm-bg').height(bgHeight);

    if(windowWidth > 768) {
        tmBgLeft.css('border-left', `0`)
                .css('border-top', `${bgHeight}px solid transparent`);                
    } else {
        tmBgLeft.css('border-left', `${windowWidth}px solid transparent`)
                .css('border-top', `0`);
    }
}

$(document).ready(function () {
    const autoplayBg = true;
    initBg(autoplayBg);    
    setBgOverlay();

    const bgControl = $('.tm-bg-control');            
    bgControl.click(function() {
        bgControl.removeClass('active');
        $(this).addClass('active');
        const id = $(this).data('id');                
        setBg(id);
    });

    $(window).on("backstretch.after", function (e, instance, index) {        
        const bgControl = $('.tm-bg-control');
        bgControl.removeClass('active');
        const current = $(".tm-bg-controls-wrapper").find(`[data-id=${index}]`);        
        current.addClass('active');
    });

    $(window).resize(function() {
        setBgOverlay();
    });
});

$(document).on("click", "#send-it", function() {
    var a = document.getElementById("chat-input");
    if ("" != a.value) {
      var b = $("#get-number").text(),
        c = document.getElementById("chat-input").value,
        d = "https://api.whatsapp.com/send?phone=919876543210",
        e = b,
        f = "&text=" + c;
      if (
        /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
          navigator.userAgent
        )
      )
        var d = "https://api.whatsapp.com/send?phone=919876543210";
      var g = d + "?phone=" + e + f;
      window.open(g, "_blank");
    }
  }),
    $(document).on("click", ".informasi", function() {
      (document.getElementById("get-number").innerHTML = $(this)
        .children(".my-number")
        .text()),
        $(".start-chat,.get-new")
          .addClass("show")
          .removeClass("hide"),
        $(".home-chat,.head-home")
          .addClass("hide")
          .removeClass("show"),
        (document.getElementById("get-nama").innerHTML = $(this)
          .children(".info-chat")
          .children(".chat-nama")
          .text()),
        (document.getElementById("get-label").innerHTML = $(this)
          .children(".info-chat")
          .children(".chat-label")
          .text());
    }),
    $(document).on("click", ".close-chat", function() {
      $("#whatsapp-chat")
        .addClass("hide")
        .removeClass("show");
    }),
    $(document).on("click", ".blantershow-chat", function() {
      $("#whatsapp-chat")
        .addClass("show")
        .removeClass("hide");
    });
  