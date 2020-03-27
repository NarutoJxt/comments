$(document).ready(function () {

    $('.commentArticle').click(function () {
        $("#c_id").attr("value",null);
        $('html,body').animate({ scrollTop: document.getElementsByTagName('BODY')[0].scrollHeight}, 2000);

        return false;
    });
    $('.replyComment').click(function () {
        c_id = $.trim($(this).parent().prev().prev().text());
        console.log(c_id)
        $('html,body').animate({ scrollTop: document.getElementsByTagName('BODY')[0].scrollHeight}, 2000);
        $("#c_id").attr("value",c_id);
        return false;
    });

})
//     let oBtn = document.querySelector("button");
//     var speed = 20;
//     oBtn.onclick = function () {
//         time = setInterval(function () {
//             var scrollHeight = document.documentElement.scrollHeight;
//             var clientHeight = document.documentElement.clientHeight;
//             var scrollTop = document.documentElement.scrollTop;
//             var scrollBottom = scrollHeight - clientHeight - scrollTop;
//             scrollBottom -= speed;
//             if (scrollBottom <= 1000) {//当滚动条距离顶部1000时，让速度变慢
//                 speed = 5;
//
//             }
//             if (scrollBottom <= 0) {
//                 clearInterval(time);
//             }
//         })};
function changeIconClick(n) {
    var img = n.children[0];
    img.setAttribute("src", "http://127.0.0.1:8000/static/icon/comment_click.png");
}
function changeIconOut(n) {
    var img = n.children[0];
    img.setAttribute("src", "http://127.0.0.1:8000/static/icon/comment_show.png");
}