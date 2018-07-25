function logout() {
    $.get("/api/logout", function(data){
        if (0 == data.errcode) {
            location.href = "/";
        }
    })
}

$(document).ready(function(){
    $.get("/api/profile", function(data) {
        if ("4101" == data.errcode) {
            location.href = "/login.html";
        }
        else if ("0" == data.errcode) {
            $("#user-name").html(data.data.name);
            $("#user-mobile").html(data.data.mobile);
            if (data.data.avatar) {
                $("#user-avatar").attr("src", data.data.avatar);
            }
        }
    }, "json");
})