function getarg()
{
	if(window.location.search != "")
	{
		var allargs = window.location.search.split("?")[1];
		var args = allargs.split("&");
		for(var i=0; i<args.length; i++)
		{
			var arg = args[i].split("=");
			eval('this.'+arg[0]+'="'+arg[1]+'";');
		}
	}
}

function setCookie30Days(name,value)
{
    var Days = 30;
    var exp  = new Date();
    exp.setTime(exp.getTime() + Days*24*60*60*1000);
    document.cookie = name + "="+ escape (value) + ";expires=" + exp.toGMTString();
}

var dvr_saved_usr = new Array();
var dvr_sa = null;
$(document).ready(function(){
	get_devinfo();
	
	var str = Cookies.get("lxc_save");
	if(str != null)
	{
		var strs = str.split(",");
		for(var i = 0; i < strs.length/2; i++)
		{
			dvr_saved_usr.push(new Array(strs[i*2 + 0], strs[i*2 + 1]));
		}
		dvr_sa = new autosuggest(
			"dvr_usr", 
			dvr_saved_usr, 
			null, 
			function(index, control) 
			{ 
				$("#dvr_usr")[0].value = control.keywords[index]; 
				$("#dvr_pwd")[0].value = control.values[index];
			});
	}
});

function show_suggest()
{
	$("#dvr_usr")[0].value = "";
	dvr_sa.timer = setTimeout(function(){dvr_sa.preSuggest(-1);},25);
}

function get_devinfo()
{
	var clientport_tag = "httpport";
	if(location.search != "")
	{
		clientport_tag = "rhttpport";
	}


	var xmldoc = loadXMLString("<juan ver=\"0\" squ=\"abcdef\" dir=\"0\" enc=\"1\"><devinfo camcnt=\"\" sensorcnt=\"\" " + clientport_tag + "=\"\" /></juan>");
	var xmlstr = toXMLString(xmldoc);
	var devinfo_node;
	var camcnt_attr;
	var camcnt_value;
	var sensorcnt_attr;
	var sensorcnt_value;
	var clientport_attr;
	var clientport_value;

	//var n1 = xmldoc.selectSingleNode("/juan/devinfo").attributes.getNamedItem("lang").nodeValue;
	//alert(n1);

	$.ajax({ 
		type:"GET",
		url: "/cgi-bin/gw.cgi", 
		processData: false, 
		cache: false,
		data: "xml=" + xmlstr, 
		async:true,
		beforeSend: function(XMLHttpRequest){
			//alert("beforeSend");
		},
		success: function(data, textStatus){
			//alert("recv:" + data);
			xmldoc = loadXMLString(data);
			
			if(xmldoc && xmldoc.getElementsByTagName("juan"))
			{
				devinfo_node = xmldoc.getElementsByTagName("juan")[0].getElementsByTagName("devinfo")[0];
				camcnt_value = devinfo_node.getAttribute("camcnt");
				sensorcnt_value = devinfo_node.getAttribute("sensorcnt");
				clientport_value = devinfo_node.getAttribute(clientport_tag);
			}

			Cookies.set("dvr_camcnt", camcnt_value);
			Cookies.set("dvr_clientport", clientport_value);
			Cookies.set("dvr_sensorcnt", sensorcnt_value);
			
			language_show_page("index_title");

			var urlarg=new getarg();
			if(urlarg.usr)
			{
				$("#dvr_usr")[0].value = urlarg.usr;
			}
			if(urlarg.pwd)
			{
				$("#dvr_pwd")[0].value = urlarg.pwd;
			}
			if(urlarg.usr || urlarg.pwd)
			{
				login_chk_usr_pwd();
			}
		},
		complete: function(XMLHttpRequest, textStatus){
			//alert("complete:" + textStatus);
		},
		error: function(XMLHttpRequest, textStatus, errorThrown){
			alert(language_find("alert_Communication_error_please_refresh_or_try_again_later"));	
		}
	});	
}

function check_os_and_browser()
{
	var ua = navigator.userAgent;
	var ret = new Object();
	if(/MSIE/i.test(ua) == true)
	{
		ret.os = "windows";
		if(/MSIE 10/i.test( ua ) == true)
		{
			ret.browser = "ie9";
		}
		else if(/MSIE 9/i.test( ua ) == true)
		{
			ret.browser = "ie9";
		}
		else if(/MSIE 8/i.test( ua ) == true)
		{
			ret.browser = "ie8";
		}
		else if(/MSIE 7/i.test( ua ) == true)
		{
			ret.browser = "ie7";
		}
		else if(/MSIE 6/i.test( ua ) == true)
		{
			ret.browser = "ie6";
		}
		else
		{
			ret.browser = "ie";
		}
	}
	else if(/Chrome/i.test( ua ) == true)
	{
		ret.browser = "chrome";
		if(/Macintosh/i.test( ua ) == true)
		{
			ret.os = "mac";
		}
		else if(/Windows/i.test( ua ) == true)
		{
			ret.os = "windows";
		}
		else if(/Android/i.test( ua ) == true)
		{
			ret.os = "android";
		}
		else if(/Linux/i.test( ua ) == true)
		{
			ret.os = "linux";
		}
		else
		{
			ret.os = "";
		}	
	}
	else if(/Safari/i.test( ua ) == true)
	{
		ret.browser = "safari";
		if(/Macintosh/i.test( ua ) == true)
		{
			ret.os = "mac";
		}
		else if(/iPhone/i.test( ua ) == true)
		{
			ret.os = "iphone";
		}
		else if(/iPad/i.test( ua ) == true)
		{
			ret.os = "ipad";
		}
		else if(/Windows/i.test( ua ) == true)
		{
			ret.os = "windows";
		}
		else if(/Android/i.test( ua ) == true)
		{
			ret.os = "android";
		}
		else if(/Linux/i.test( ua ) == true)
		{
			ret.os = "linux";
		}
		else
		{
			ret.os = "";
		}
	}
	else if(/Firefox/i.test( ua ) == true)
	{
		ret.browser = "firefox";
		if(/Macintosh/i.test( ua ) == true)
		{
			ret.os = "mac";
		}
		else if(/Windows/i.test( ua ) == true)
		{
			ret.os = "windows";
		}
		else if(/Linux/i.test( ua ) == true)
		{
			ret.os = "linux";
		}
		else
		{
			ret.os = "";
		}
	}
	else if((/Windows/i.test(ua)) && (/Trident/i.test(ua)) && (/rv:11.0/i.test(ua)))
	{
		ret.os = "Windows";
		ret.browser = "ie11";
	}
	else
	{
		ret.browser = "";
		ret.os = "";
	}
	
//	if(ret.os == "" || ret.browser == "")
//	{
//		alert(ua);	
//	}
//	alert("os="+ret.os+",browser="+ret.browser);
	return ret;
}

function save_usr(_usr, _pwd)
{
	//save
	var modified = false;		
	for(var i = 0; i < dvr_saved_usr.length; i++)
	{
		if(dvr_saved_usr[i][0] == _usr) //modify
		{
			dvr_saved_usr[i][1] = _pwd;
			modified = true;
			break;
		}
	}
	if(modified == false) //add
	{
		dvr_saved_usr.push(new Array(_usr, _pwd));
	}
}

function del_usr(_usr)
{
	//delete
	for(var i = 0; i < dvr_saved_usr.length; i++)
	{
		if(dvr_saved_usr[i][0] == _usr)
		{
			dvr_saved_usr.splice(i, 1);
			break;
		}
	}
}
var timeunlock
function set_timeunlock(locktime)
{	
	timeunlock=locktime;
	if(timeunlock>0)
	{
		
		var lockhour=parseInt(timeunlock/3600);
		var lockmin=parseInt(timeunlock%3600/60);
		var locksec=parseInt(timeunlock%60);
		document.getElementById("time_txt").innerHTML=language_find("alert_Lock")+lockhour+":"+lockmin+":"+locksec;
		timeunlock--;
		setTimeout(function() { 
			set_timeunlock(timeunlock) 
			},1000)
	}
	else
	{
			EV_closeAlert();
			return;
	}
		
	 
	
}
var iSetAble,iPlayBack;
document.write("<script language=javascript src='js/dialog.js'></script>");
function login_chk_usr_pwd()
{
	var dvr_usr = $("#dvr_usr")[0].value;
	var dvr_pwd = $("#dvr_pwd")[0].value;

	if(dvr_usr != "")
	{
		if($("#dvr_remember")[0].checked == true)
		{
			save_usr(dvr_usr, dvr_pwd);
		}
		else
		{
			del_usr(dvr_usr);
		}
	}
	//alert(dvr_saved_usr.join());
	setCookie30Days("lxc_save", dvr_saved_usr.join());

	var xmldoc = loadXMLString("<juan ver=\"\" squ=\"\" dir=\"0\"><rpermission usr=\"" + dvr_usr + "\" pwd=\"" + dvr_pwd + "\" ><config base=\"\" /><playback base=\"\" /></rpermission></juan>");
	var xmlstr = toXMLString(xmldoc);
	var envload_node;
	var errno_attr;
	var errno_value;
	var oSetAble,oPlayBack;
	var remaintry;
	var locktime;
	$.ajax({ 
		type:"GET",
		url: "/cgi-bin/gw.cgi", 
		processData: false, 
		cache: false,
		data: "xml=" + xmlstr, 
		async:true,
		beforeSend: function(XMLHttpRequest){
			//alert("beforeSend");
		},
		success: function(data, textStatus){
			//alert("recv:" + data);
			xmldoc = loadXMLString(data);
			if(xmldoc && xmldoc.getElementsByTagName("juan"))
			{
				envload_node = xmldoc.getElementsByTagName("juan")[0].getElementsByTagName("rpermission")[0];
				errno_value = envload_node.getAttribute("errno");
				remaintry=envload_node.getAttribute("remain");
				locktime=envload_node.getAttribute("locktime");
				if(errno_value == "0")
				{
					oSetAble = xmldoc.getElementsByTagName('juan')[0].getElementsByTagName('config')[0];
					iSetAble = oSetAble.getAttribute('base');
	
					oPlayBack = xmldoc.getElementsByTagName('juan')[0].getElementsByTagName('playback')[0];
					iPlayBack = oPlayBack.getAttribute('base');

					login_set(dvr_usr,dvr_pwd,iSetAble,iPlayBack);
					
					var os_browser = check_os_and_browser();
					if(os_browser.browser == "ie6" || os_browser.browser == "ie7" || os_browser.browser == "ie8" || os_browser.browser == "ie9" || os_browser.browser == "ie10" || os_browser.browser == "ie11" )
					{
						location.replace("view1.html");
					}
					else
					{
						location.replace("view2.html");
					}
				}
				else
				{
					if(remaintry>0)
					{
						alert(language_find("alert_Username_or_password_error")+language_find("alert_remain_input_time")+remaintry);
					}
					else if(remaintry==0)
					{
						if(locktime>0)
						{
						set_timeunlock(locktime);
						EV_modeAlert('timelocker');
						}
						
						//alert("i'am in ");
						//alert("lock!!\r\n"+lockhour+":"+lockmin+":"+locksec);
						//alert(locktime);
					}else if(remaintry==-1)
					{
						
						alert(language_find("alert_Username_inexistence"));
					}else
					{
						
						alert(language_find("alert_Username_or_password_error"));
					}
				}
			}
		},
		complete: function(XMLHttpRequest, textStatus){
			//alert("complete:" + textStatus);
		},
		error: function(XMLHttpRequest, textStatus, errorThrown){
			alert(language_find("alert_Communication_error_please_refresh_or_try_again_later"));	
		}
	});
}

