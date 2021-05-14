const downBtn = document.querySelector("#downloadBtn");
const extension = document.querySelector("#extension");
const body = document.querySelector("#main");
var progress = 0
var interval  = 0



downBtn.addEventListener('click', function(){
    if(extension.value == ""){
        alert('اختر صيغة الكتب أولاً')
    } else {
        eel.download(extension.value)(cb)
        $.LoadingOverlay("show", {
            text: ".جارٍ التحميل ... قد يستغرق  تحميل المكتبة كاملة عدة ساعات، لا تغلق هذه النافذة أو تطفئ الجهاز",
            textResizeFactor        : 0.1,
        });
    }
})

function cb(val){
    $.LoadingOverlay("hide");
    body.innerHTML = '<p style="font-family: Amiri, serif; font-weight: bold; text-align: center">اكتمل التحميل </p><span> <img src="assets/img/check.png" style="width: 100%;margin: 0px;mix-blend-mode: multiply;"></span>';
            
}