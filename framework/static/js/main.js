/**
  * 增加标签页
  */
function menuClick(tabCode, tabName, tabUrl) {
	var options={
		tabMainName:"tab-title-main",
		tabContentMainName:"tab-content-main",
		tabCode:tabCode,
		tabName:tabName,
		tabUrl:tabUrl
	};
	addTab(options);
};
/**
  * 增加标签页
  */
function addTab(options) {			
     //option:
     //tabMainName:tab标签页所在的容器
     //tabContentMainName:tab标签页的内容所在容器
     //tabCode:当前tab的名称
     //tabName:当前tab的标题
     //tabUrl:当前tab所指向的URL地址
     var exists = checkTabIsExists(options.tabMainName, options.tabCode);
     if(exists){
         $("#tab_title_"+options.tabCode).click();
     } else {
         $("#"+options.tabMainName).append('<a class="red item" id="tab_title_'+options.tabCode+'" data-tab="tab_content_'+options.tabCode+'">'+options.tabName+'<i class="close link icon" onclick="closeTab(this);"></i></a>');
         var content = '';
         if(options.content){
             content = option.content;
         } else {
             content = '<iframe src="' + options.tabUrl + '" width="100%" frameborder="no" border="0" marginwidth="0" onload="setIframeHeight(this)"></iframe>';
         }
         
         $("#"+options.tabContentMainName).append('<div class="ui tab" id="tab_content_'+options.tabCode+'" data-tab="tab_content_'+options.tabCode+'">'+content+'</div>');
         $(".menu .item").tab();   
         $("#tab_title_"+options.tabCode).click();
     }
};
 /**
  * 关闭标签页
  * @param button
  */
function closeTab(button) {    
	var tab_title_id = $(button).parent().attr('id');
	var id = tab_title_id.replace("tab_title_","");

	//如果关闭的是当前激活的TAB，激活他的前一个TAB
	if ($("#" + tab_title_id).hasClass("active")) {
		alert("111");
	    $("#" + tab_title_id).prev().click();
	}
 
	//关闭TAB
	$("#" + tab_title_id).remove();
	$("#tab_content_" + id).remove();
};
 
		/**
 * 判断是否存在指定的标签页
 * @param tabMainName
 * @param tabCode
 * @returns {Boolean}
 */
function checkTabIsExists(tabMainName, tabCode){
    var tab = $("#"+tabMainName+" > #tab_title_"+tabCode);
    //console.log(tab.length)
    return tab.length > 0;
}

