/**
  * 增加标签页
  */
function menuClick(tabCode, tabName, tabUrl) {
	alert("1111");
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
         $("#"+options.tabMainName).append('<a class="red item" data-tab="eight">'+options.tabName+'<i class="close link icon"></i></a>');
         var content = '';
         if(options.content){
             content = option.content;
         } else {
             content = '<iframe src="' + options.tabUrl + '" width="100%" frameborder="no" border="0" marginwidth="0" onload="setIframeHeight(this)"></iframe>';
         }
         $("#"+options.tabContentMainName).append('<div id="tab_content_'+options.tabCode+'" role="tabpanel" class="tab-pane" id="'+options.tabCode+'">'+content+'</div>');
         $("#tab_a_"+options.tabCode).click();
     }
};
 /**
  * 关闭标签页
  * @param button
  */
function closeTab (button) {    
	var li_id = $(button).parent().parent().attr('id');
	var id = li_id.replace("tab_li_","");
	 
	//如果关闭的是当前激活的TAB，激活他的前一个TAB
	if ($("li.active").attr('id') == li_id) {
	    $("li.active").prev().find("a").click();
			}
 
			//关闭TAB
	$("#" + li_id).remove();
	$("#tab_content_" + id).remove();
};
 
		/**
 * 判断是否存在指定的标签页
 * @param tabMainName
 * @param tabCode
 * @returns {Boolean}
 */
function checkTabIsExists(tabMainName, tabCode){
    var tab = $("#"+tabMainName+" > #tab_li_"+tabCode);
    //console.log(tab.length)
    return tab.length > 0;
}

