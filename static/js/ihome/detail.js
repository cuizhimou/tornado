function hrefBack() {
    history.go(-1);
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

$(document).ready(function(){
    var house_id = decodeQuery()["id"];
    $.get("/api/house/info?house_id="+house_id, function (data) {
        if ("0" == data.errcode) {
            $(".swiper-container").html(template("house-image-tmpl", {"img_urls":data.data.images, "price":data.data.price}));
            $(".detail-con").html(template("house-detail-tmpl", {"house":data.data}));
            var mySwiper = new Swiper ('.swiper-container', {
                loop: true,
                autoplay: 2000,
                autoplayDisableOnInteraction: false,
                pagination: '.swiper-pagination',
                paginationType: 'fraction'
            })
            // data.user_id为访问页面用户,data.data.user_id为房东
            if (data.user_id != data.data.user_id) {
                $(".book-house").attr("href", "/booking.html?hid="+house_id);
                $(".book-house").show();
            }
        }
    }, "json")
})