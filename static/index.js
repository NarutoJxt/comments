"点击时加深评论图标颜色"
function changeIconClick(n) {
    var img = n.children[0].children[0];
    img.setAttribute("src", "http://127.0.0.1:8000/static/icon/comment_click.png");
}
function changeIconOut(n) {
    var img = n.children[0].children[0];
    img.setAttribute("src", "http://127.0.0.1:8000/static/icon/comment_show.png");
}
$(document).ready(function() {
        $("#editArticleForm").hide();

        $("button#showFom").click(
            function () {
                console.log("sss");
                $("#editArticleForm").slideToggle();
            }
        );
    }
);