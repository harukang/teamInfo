jQuery(document).ready(function(){
 
  
  $(".myimg li").click(function(){
    $("#modal").addClass("active")
})
$("#close").click(function(){
  $("#modal").removeClass("active")
})
$("#modal_bg").click(function(){
  $("#modal").removeClass("active")
})

  $(".plusbtn").click(function(){
    $("#img_at").addClass("active")
  })
  $("#img_at_bg").click(function(){
    $("#img_at").removeClass("active")
  })

})