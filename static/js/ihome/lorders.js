//模态框居中的控制
function centerModals(){
    $('.modal').each(function(i){   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');    
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top-30);  //修正原先已经有的30个像素
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);
    $.get("/api/order/my?role=landlord", function(data){
        if ("0" == data.errcode) {
            $(".orders-list").html(template("orders-list-tmpl", {orders:data.orders}));
            $(".order-accept").on("click", function(){
                var orderId = $(this).parents("li").attr("order-id");
                $(".modal-accept").attr("order-id", orderId);
            });
            $(".modal-accept").on("click", function(){
                var orderId = $(this).attr("order-id");
                $.ajax({
                    url:"/api/order/accept",
                    type:"POST",
                    data:'{"order_id":'+ orderId +'}',
                    contentType:"application/json",
                    headers:{
                        "X-XSRFTOKEN":getCookie("_xsrf"),
                    },
                    dataType:"json",
                    success:function (data) {
                        if ("4101" == data.errcode) {
                            location.href = "/login.html";
                        } else if ("0" == data.errcode) {
                            $(".orders-list>li[order-id="+ orderId +"]>div.order-content>div.order-text>ul li:eq(4)>span").html("已接单");
                            $("ul.orders-list>li[order-id="+ orderId +"]>div.order-title>div.order-operate").hide();
                            $("#accept-modal").modal("hide");
                        }
                    }
                })
            });
            $(".order-reject").on("click", function(){
                var orderId = $(this).parents("li").attr("order-id");
                $(".modal-reject").attr("order-id", orderId);
            });
            $(".modal-reject").on("click", function(){
                var orderId = $(this).attr("order-id");
                var reject_reason = $("#reject-reason").val()
                if (!reject_reason) return;
                var data = {
                    order_id:orderId,
                    reject_reason:reject_reason
                };
                $.ajax({
                    url:"/api/order/reject",
                    type:"POST",
                    data:JSON.stringify(data),
                    contentType:"application/json",
                    dataType:"json",
                    headers: {
                        "X-XSRFTOKEN":getCookie("_xsrf"),
                    },
                    success:function (data) {
                        if ("4101" == data.errcode) {
                            location.href = "/login.html";
                        } else if ("0" == data.errcode) {
                            $(".orders-list>li[order-id="+ orderId +"]>div.order-content>div.order-text>ul li:eq(4)>span").html("已拒单");
                            $(".order-operate").hide();
                            $("#reject-modal").modal("hide");
                        }
                    }
                });
            })
        }
    });
});