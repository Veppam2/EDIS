/**
 * Initialize Carrousel
 */
function initDealCarrousel(dealCarrouselID) {
    var target = document.querySelector("#" + dealCarrouselID + " .va-carrousel-flexbox");
    var cardOutterWidth;
    var maxCarrouselScroll;
  
    function updateUpaCarrouselInfo() {
      cardOutterWidth = document.querySelector("#" + dealCarrouselID + " .va-card").offsetWidth; //you can define how far the scroll
      maxCarrouselScroll = (document.querySelectorAll("#" + dealCarrouselID + " .va-card").length *
      cardOutterWidth) - document.querySelector("#" + dealCarrouselID + " .va-carrousel-flexbox")
      .clientWidth;
    }
  
    document.querySelector("#" + dealCarrouselID + " .deals-scroll-left").addEventListener("click",
      function () {
        updateUpaCarrouselInfo(); //in case window resized, will get new info
        if (target.scrollLeft > 0) {
          scrollLeftAnimate(target, -cardOutterWidth * 2);
        }
      }
    );
  
    document.querySelector("#" + dealCarrouselID + " .deals-scroll-right").addEventListener("click",
      function () {
        updateUpaCarrouselInfo(); //in case window resized, will get new info 
        if (target.scrollLeft < maxCarrouselScroll) {
          scrollLeftAnimate(target, cardOutterWidth * 2);
        }
      }
    );
  }
  // Initiate the container with ID
  initDealCarrousel('va_container'); //carrousel ID