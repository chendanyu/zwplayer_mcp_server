"""
FastMCP Echo Server
"""

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.server import Settings

# Create server

# Stateful server (maintains session state)
# mcp = FastMCP("StatefulServer")

# Stateless server (no session persistence)
mcp = FastMCP("StatelessServer", stateless_http=True)

settings=Settings()

settings.debug = True
settings.host = "0.0.0.0"
settings.port = 30002
# set
mcp.settings=settings

# Stateless server (no session persistence, no sse stream with supported client)
# mcp = FastMCP("StatelessServer", stateless_http=True, json_response=True)

# 运行
# python streamable_echo_server.py

@mcp.tool()

    
@mcp.tool()
def zwplayer_indroduce() -> str:
    """zwplayer的介绍"""
    introduce = """
        zwplayer是一款基于HTML5的Web网页播放器，是一款简单易用的H5媒体播放器。zwplayer为 H5 视频播放应用开发者提供一个零成本、简单易用、具备丰富协议支持、功能丰富与界面美观的Web 播放器，以降低Web应用开发者的时间成本，加速项目进度。zwplayer为开发者完成一个Web播放器完整的操作界面开发，提供了一个跨浏览器一致性的操作界面。
        部分功能列表:
        1.全功能播放器，支持点播流与直播流
        2.点播流支持 MP4、hls、dash等协议播放
        3.直播流支持：http-flv、hls、dash、http-ts等所有当前流行协议
        4.支持webrtc低延时直播播放
        5.支持 rtsp协议转发技术，能在H5网页里直接播放rtsp流
        6.支持多码流(视频清晰度)切换，对 hls、dash 等协议支持多码流自适应切换
        7.支持多种格式字幕，支持 vtt、srt、json与bcc 等格式的外挂字幕，支持hls、dash等流内嵌字幕的提取与选择控制
        8.支持双字幕同时渲染（多语言字幕），用户随意选择需要显示的单个字幕或全部字幕
        9.内建完整的弹幕支持，包含弹幕渲染与弹幕设置
        10.支持预览缩略图，在播放进度条上滑动鼠标，可以预览视频内容
        11.支持网页全屏、画中画与自动小窗口等播放操作界面
        12.支持视频画面多角度旋转，包括正反转180度，正反转90度等
        13.支持图像截取，支持截图直接上传功能
        14.支持设置自定义logo
        15.支持点播流速率调节
        16.支持播放过程中问答弹出功能
        17.支持点播节目章节（关键点）打点
        18.支持自动播放预探测技术，完美解决当今浏览器未设置静音时自动播放操作在用户发起交互操作前失败的难题
        19.支持禁止拖动播放进度
        20.支持视频颜色属性调节，包括亮度、对比度、色调与饱和度
        21.免插件调用，功能全内置，播放扩展协议无需手工设置插件，调用简单
        22.开发调用简单，较少的API，整合简单容易，只需简单配置即可使用播放器
        23.升级简单，永久固化的API，使后续升级只须简单替换文件即可，代码零改动
        24.完全独立的库，无需其它第三方js库调用，不依赖于jQuery等任何第三方js库，集成简易
        25.完全免费使用，没有任何限制，无论个人还是商业使用
        26.非常容易集成，仅须引用一个js文件
        27.轻量级高性能，所有外部扩展模块动态智能加载，不用到的不会预先加载，加速网页加载
        28.可扩展的平台支持，多种编码、多种协议与跨浏览器跨平台
        29.支持vue2，vue3
    """
    return introduce
    
@mcp.tool()
def zwplayer_base() -> str:
    """zwplayer的基本使用"""
    script = """
        <script type="text/javascript" charset="utf-8" src="/zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
	
        <script type="text/javascript">
            var info = {
                playerElm: 'mse',
                url: 'https://d2zihajmogu5jn.cloudfront.net/elephantsdream/ed_hd.mp4',
                videostyle: "width:100%;height:80%;",
            };
            new ZWPlayer(info);
        </script>
        
        demo: 
    """
    return script   


@mcp.tool()
def zwplayer_width_height() -> str:
    """zwplayer指定播放的宽高"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
	
        <script type="text/javascript">
            var info = {
                playerElm: 'mse',
                url: 'https://d2zihajmogu5jn.cloudfront.net/elephantsdream/ed_hd.mp4',
                videostyle: "width:100%;height:80%;",
            };
            new ZWPlayer(info);
        </script>
        
        demo: <a href="unit02_width_height.html">zwplayer指定播放的宽高</a>
    """
    return script  


@mcp.tool()
def zwplayer_fluid() -> str:
    """zwplayer 支持流体布局"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="video_contain" style=""></div>
        <script type="text/javascript">
            var info = {
                playerElm: 'video_contain',
                url: 'https://d2zihajmogu5jn.cloudfront.net/elephantsdream/ed_hd.mp4',
                fluid: true,
                ratio:"16:9",
            };
            new ZWPlayer(info);
        </script>
        
        demo: <a href="unit03_fluid.html">zwplayer支持流体布局</a>
    """
    return script    


@mcp.tool()
def zwplayer_poster() -> str:
    """zwplayer 支持设置海报"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
			<script type="text/javascript">
			var info = {
				playerElm: 'mse',
				url: 'https://d2zihajmogu5jn.cloudfront.net/elephantsdream/ed_hd.mp4',
				poster: 'https://aigc-image.bj.bcebos.com/miaobi/5mao/b%276buR5oKf56m65pmu6YCa54mI5ZKM6LGq5Y2O54mI5Yy65YirXzE3MjQ4NjE5NzUuMzcyNjEzXzE3MjQ4NjE5NzYuMTI0MTA0%27/1.png',
				logo: {
					icon: 'https://www.ckplayer.com/public/static/ckplayer-x3/css/images/logo.png',
					dock: 'right',
					x: '5%',
					y: '5%',
					width: '10%',
					height: '10%',
					opacity: 70
				},
				autoplay: false,

			};
			new ZWPlayer(info);
		</script>
        
        demo: <a href="unit04_poster_logo.html">zwplayer设置海报</a>
    """
    return script    


@mcp.tool()
def zwplayer_subtitle() -> str:
    """zwplayer 设置字幕"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
        <script type="text/javascript">
			function onLoadSubtitle() {
				if (player1) {
					//var subtitleUrl = 'http://192.168.1.202:8088/data/VMAP9RxJk5Fon5g83BxAmB1gmh8$hktnmQ04jN53h2.srt';
					//  var subtitleURL_korean = 'https://www.zwplayer.cn/uploadfile/test/VMAP9lxJvRpgn5sP3lV6rQ9qkzQmh5psggtFawR3lNR7hQ2_kore.srt';
					//  var subtitleURL_japan = 'https://www.zwplayer.cn/uploadfile/test/VMAP9lxJvRpgn5sP3lV6rQ9qkzQmh5psggtFawR3lNR7hQ2_jpan.srt';
					var subtitleURL_en = './zwplayer/video/en.vtt';
					var subtitleURL_zh = './zwplayer/video/zh.vtt';
					player1.addSubtitle(subtitleURL_en, '1');
					player1.addSubtitle(subtitleURL_zh, '2');
				}
			}


			// 定义一个js对象info ，用来做为ZWPlayer 的构造参数
			var info = {
				playerElm: '#mse',
				autoplay: true,
				url: 'https://d2zihajmogu5jn.cloudfront.net/elephantsdream/ed_hd.mp4',
			};
			//创建一个播放器实例
			var player1 = new ZWPlayer(info);
			//启动播放，zwplayer默认是自动启动播放的，因此，也建议省略下行代码
			//仅在构造参数的autoplay设置为false时才需要调用
			// player1.play();


			setTimeout(onLoadSubtitle, 1000);
		</script>
        
        demo: <a href="unit05_subtitle.html">zwplayer设置字幕</a>
    """
    return script 


@mcp.tool()
def zwplayer_bullet_comments() -> str:
    """zwplayer 设置弹幕"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
        <script type="text/javascript">
			function onOpenUrl(urlObj) {
        var url;
        var streamtype = "";

        if (urlObj) {
            url = urlObj;
        }
          
        var timer = new Date();
        var timeStart = timer.getTime() - 1686800000000;
         

        if (!window.zwplayer) {
            //var playerDom = document.querySelector('#player-holder');
            window.zwplayer = new ZWPlayer({
              url:url,
              playerElm:'#mse', //player 元素ID ,也可以直接的DOM对象 playerDom
             
         
              fluid: false,
              
              muted: false,
              onready:function() {
                console.log("Player onready");

              },
              onfirstframe:function() {
                console.log("Player onfirstframe");
              },
              onnetclose:function() {
                console.log("Player onnetclose");
              },
              onneterror:function() {
                console.log("Player onneterror");
              },
              onmediaevent: function(event) {
                if (['play', 'pause', 'seeked', 'ended', 'error'].includes(event.type)) {
                    console.log("player video Event:", event);
                    if (event.type == 'seeked') {
                        var currentTime = event.srcElement.currentTime;

                        console.log("player currentTime:", currentTime);
                    }

                    if (event.type === 'play') {
                        var timeEnd = (new Date()).getTime() - 1686800000000;
                        var timeTotal = timeEnd - timeStart;
                        
                        console.log("timeEnd:", timeEnd);
                        console.log("timeTotal:", timeTotal);
                    }
                }
              },
              sendDanmu: function(text) {
                //alert(text);
                if (typeof window.ws_send === 'function') {
                    window.ws_send(text);
                }
              }
          });

          window.zwplayer.buildDanmuControlbar('player-dammu-controlbar');
        }
        else {
            window.zwplayer.play(url, isLive, false);
        }
    }

    function onload() {
         
        var url = 'https://d2zihajmogu5jn.cloudfront.net/elephantsdream/ed_hd.mp4';
        // url = 'http://192.168.1.136:1966/live/stream007.rtc';

         
        setTimeout(function() {
            //alert('ok');
            onOpenUrl(url);
        }, 100);

        //new VConsole();
    }

    window.channelinfo = {
        id: '001'
    };

    (function(root) {
        var wsChat = null;
        var logView = null;
        var wschat_server = 'ws://122.51.191.171:3000/';//"ws://192.168.1.202:9168/";
        var reconnect = false;
        var msg_queue = [];
        var force_close = false;
        var userCurrent = {};


        function chat_log(str) {
            console.log(str);
        }

        function toast(type, msg) {

        }

        root.ws_init = function chatSocketInit() {

            if (wsChat) return wsChat;
            // Connect to Web Socket.
            // Change host/port here to your own Web Socket server.
            try {
                wsChat = new WebSocket(wschat_server);
            }
            catch(e) {
                return false;
                reconnect = false;
            }

            // Set event handlers.
            wsChat.onopen = function() {
                chat_log("wsChat onopen");

                if (window.enableBalance=='1' && !window.mediaserver) {
                    root.ws_getmediaserver();
                }

                window.setTimeout(function() {
                    delete userCurrent.loginChat;
                    if (!wsChat) return;
                    wsChat.send('{type:"hello"}');

                    if (reconnect) {
                        toast('showToast', {
                            text     : '与互动服务器的重新建立连接成功。',
                            sticky   : false,
                            stayTime : 3000,
                            position : 'top-center',
                            type     : 'notice'
                        });
                        reconnect = false;
                        if (msg_queue['userlogin']) {
                            wsChat.send(msg_queue['userlogin']);
                            delete msg_queue['userlogin'];
                        }
                    }
                },40);
            };


            wsChat.onmessage = function(e) {
                // e.data contains received string.
                chat_log("wsChat onmessage: " + e.data);

                if (e.data.length > 0) {
                    if (e.data.charAt(0) === '{') {
                        var msgContent;
                        var msgObj = JSON.parse(e.data);

                        if (typeof (msgObj) === 'object') {
                            if (msgObj.text)
                                msgContent = msgObj.text;
                            else
                                msgContent = '';

                            if (msgObj.type === 'danmu') {
                                if (window.zwplayer) {

                                    if (msgContent == '') return ;
                                    // msgObj.text = msgContent;
                                    window.zwplayer.appendDanmu(msgObj);
                                }
                            }
                            else if (msgObj.type === 'hello') {
                                window.joinRoomOk = true;
                                //获得授予的UID
                                window.current_uid = msgObj.uid;
                                var roomname = 'videoroom_' + window.channelinfo.id;
                                window.ws_send('{"type":"join","room":"'+roomname+'"}');
                            }
                            else if (msgObj.type === 'login') {
                                if (!msgObj.result || msgObj.result != 'success') {
                                    toast('showNoticeToast', '登录到互动服务器返回不成功。<br/>可能影响聊天互动！');
                                }
                                else {
                                    userCurrent.loginChat = true;
                                }
                            }
                            else if (msgObj.type === 'logout') {
                                //用户自己登出的回馈
                                delete userCurrent.loginChat;
                            }
                            else if (msgObj.type === 'event') {
                                if (msgObj.event === 'joinroom') {
                                    //别的用户与自己连接到聊天服务器
                                    if (msgObj.uid) {
                                        if (msgObj.uid === window.current_uid) {
                                            userCurrent.joinroom = true;
                                        }
                                    }
                                }
                                else if (msgObj.event === 'leaveroom' || msgObj.event === 'exitroom') {
                                    //别的用户离开聊天服务器
                                    if (msgObj.uid) {
                                        if (msgObj.uid === window.current_uid) {
                                            userCurrent.joinroom = false;
                                        }
                                    }
                                }
                                else if (msgObj.event === 'login') {
                                    //别的用户连接到聊天服务器
                                    if (msgObj.uid) {

                                    }
                                }
                                else if (msgObj.event === 'logout') {
                                    //别的用户离开聊天服务器
                                    if (msgObj.uid) {

                                    }
                                }
                            }
                            else if (msgObj.type == 'userlist') {
                                //连接到聊天服务器后服务器马上推送在线用户列表，该列表不包括自己
                                if (msgObj.users.length > 1) {

                                }
                            }
                            else if (msgObj.type === 'setuserid') {
                                //连接建立后将收到这个事件
                                window.current_uid = msgObj.uid;
                                userCurrent.userid = msgObj.uid;
                            }
                        }
                    }
                }
            };

            wsChat.onclose = function() {
                chat_log("wsChat onclose");
                wsChat = null;
                toast('showToast', {
                    text     : '与互动服务器的连接已经断开。',
                    sticky   : false,
                    stayTime : 3000,
                    position : 'top-center',
                    type     : 'notice'
                });
                if (force_close) {


                }
                else if (!reconnect) { //当前不是重连状态，则尝试重连
                    reconnect = true; //设置为正在重连状态
                    var on_reconnect = function() {
                        if (force_close) return;

                        wschat = root.wschat = root.ws_init();
                        if (!wschat) {
                            reconnect = true;
                            window.setTimeout(on_reconnect,10000);
                        }
                    }
                    window.setTimeout(on_reconnect,10000);
                }
            };

            wsChat.onerror = function() {

                chat_log("wsChat onerror");
                wsChat = null;
            };

            return wsChat;
        }

        root.ws_send = function wsChatSend(data) {
            chat_log("wsChat send: " + data);

            if (wsChat) {
                wsChat.send(data);
                return true;
            }
            else {
                toast('showToast', {
                    text     : '聊天交互服务没有连接成功或已经中断！<br/>正在尝试重连,请稍候再试...',
                    sticky   : false,
                    stayTime : 3000,
                    position : 'top-center',
                    type     : 'warning'
                });

                reconnect = true;
                wschat = root.wschat = root.ws_init();

                return false;
            }
        }

        root.ws_queue = function wsQueue(type,msg) {
            msg_queue[type] = msg;
        }

        root.ws_close = function wsChatClose() {
            if (wsChat) {
                force_close = true;
                wsChat.close();
                wsChat = null;
            }
            else {

            }
        }

        root.wschat = wsChat;
    })(window);

    window.ws_init();
	</script>
    
    <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
    <div class="vxplayer-toolbar danmubar" id="player-dammu-controlbar"></div>
        
        demo: <a href="unit06_danmu.html">zwplayer支持弹幕</a>
    """
    return script 
    
    
@mcp.tool()
def zwplayer_thumb() -> str:
    """zwplayer 缩略图参数，缺省为未定义。缩略图为预先抓取的视频缩略图，用于当用于在进度条上移动鼠标时，显示该视频不同时间的预览画面，仅对点播节目有效。"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
		<script type="text/javascript">
			var thumbnails = {
				"url": "https://www.zwplayer.cn/uploadfile/test/b44c43c90be3521bc352aad1e80f9cd0_thumb.jpg",
				"width": 160,
				"height": 90,
				"row": 9,
				"col": 9,
				"total": 74
			};
			// 定义一个js对象info ，用来做为ZWPlayer 的构造参数
			var info = {
				playerElm: '#mse',
				autoplay: true,
				useProgressTooltip: true,
				thumbnails: thumbnails,
				url: 'https://www.zwplayer.cn/uploadfile/test/VMAP9lxJvRpgn5sP3lV6rQ9qkzQmh5psggso3185.mp4'
			};
			//创建一个播放器实例
			var player1 = new ZWPlayer(info);
		</script>
        
        demo: <a href="unit07_thumb.html">zwplayer支持设置缩略图</a>
    """
    return script     


@mcp.tool()
def zwplayer_chapter() -> str:
    """zwplayer 节目章节打点信息，缺省为未定义。chapters 参数可以是字符串，也可以是一个已经分析好的js数组。如果chapters是字符串并且是以http或https开头的，则zwplayer会把该参数当作一个章节的url，在加载时自动从远程下载；如果chapters是以字符“[” 开头的，则会被当作一个JSON数组来进行分析；如果chapters是以WEBVTT开头的，则会当作一个WEBVTT文件来处理。不建议在播放器初始化时设置该参数，推荐的方式时在播放器启动播放后通过 setChapters 方法进行延时加载。"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
		<script type="text/javascript">
			function onLoadChapters() {
				if (player1) {

					var json = [{
							"title": "分段1",
							"desc": "分段1描述",
							"time": 0,
							"duration": 5,
							"thumb": null
						},
						{
							"title": "分段2",
							"desc": "分段2描述",
							"time": 5,
							"duration": 10,
							"style": {
								"background": "blue"
							},
							"image": null
						},
						{
							"title": "分段3",
							"desc": "分段3描述",
							"time": 15,
							"duration": 10,
							"style": {
								"background": "green"
							},
							"image": null
						},


					];
					player1.setChapters(json);
				}
			}


			// 定义一个js对象info ，用来做为ZWPlayer 的构造参数
			var info = {
				playerElm: '#mse',
				autoplay: true,
				chapterButton: true,
				url: 'https://d2zihajmogu5jn.cloudfront.net/elephantsdream/ed_hd.mp4'
			};
			//创建一个播放器实例
			var player1 = new ZWPlayer(info);


			setTimeout(onLoadChapters, 300);
		</script>
        
        demo: <a href="unit08_chapter.html">zwplayer设置节目章节打点信息</a>
    """
    return script 
    
    
@mcp.tool()
def zwplayer_flv() -> str:
    """zwplayer 播放flv格式的媒体文件"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
		<script type="text/javascript">
			// 定义一个js对象info ，用来做为ZWPlayer 的构造参数
			var info = {
				playerElm: '#mse',
				autoplay: false,
				isLive: true,
				url: {
					"httpflv": '//sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/flv/xgplayer-demo-360p.flv',
				}
			}

			var player1 = new ZWPlayer(info);
		</script>
        
        demo: <a href="unit09_flv.html">zwplayer播放flv格式的媒体文件</a>
    """
    return script     
    
    
@mcp.tool()
def zwplayer_hls() -> str:
    """zwplayer 播放HLS格式的媒体文件"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
        <script type="text/javascript">
            var info = {
                playerElm: '#mse',
                autoplay:  true,
                url: 'https://d2zihajmogu5jn.cloudfront.net/elephantsdream/hls/ed_hd.m3u8',
            };
            var player1 = new ZWPlayer(info);
          
        </script>
        
        demo: <a href="unit09_hls.html">zwplayer播放HLS格式的媒体文件</a>
    """
    return script  


@mcp.tool()
def zwplayer_m3u8() -> str:
    """zwplayer 播放m3u8格式的媒体文件"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
        <script type="text/javascript">
            var info = {
                playerElm: '#mse',
                autoplay:  true,
                url: 'https://d2zihajmogu5jn.cloudfront.net/sintel/master.m3u8',
            };
            var player1 = new ZWPlayer(info);
        </script>
        
        demo: <a href="unit09_m3u8.html">zwplayer播放m3u8格式的媒体文件</a>
    """
    return script    
    
    
@mcp.tool()
def zwplayer_mpd() -> str:
    """zwplayer 播放mpd格式的媒体文件"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
        <script type="text/javascript">
            var info = {
                playerElm: '#mse',
                autoplay:  true,
                url: 'https://dash.akamaized.net/akamai/bbb_30fps/bbb_30fps.mpd',
            };
            var player1 = new ZWPlayer(info);
          
        </script>
        
        demo: <a href="unit09_mpd.html">zwplayer播放mpd格式的媒体文件</a>
    """
    return script   


@mcp.tool()
def zwplayer_ts() -> str:
    """zwplayer 播放ts格式的媒体文件"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
        <script type="text/javascript">
            var info = {
                playerElm: '#mse',
                autoplay:  true,
                url: 'https://dash.akamaized.net/akamai/bbb_30fps/bbb_30fps.ts',
            };
            var player1 = new ZWPlayer(info);
        </script>
        
        demo: <a href="unit09_ts.html">zwplayer播放ts格式的媒体文件</a>
    """
    return script   


@mcp.tool()
def zwplayer_adaptive_bitrate() -> str:
    """zwplayer 自适应码流"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
		<script type="text/javascript">
			var info = {
				playerElm: '#mse',
				autoplay: true,
				url: [{
					name: '超清',
					url: '//sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-720p.mp4'
				}, {
					name: '高清',
					url: '//sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-480p.mp4'
				}, {
					name: '标清',
					url: '//sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-360p.mp4'
				}],
			};
			var player1 = new ZWPlayer(info);
		 
		</script>
        
        demo: <a href="unit10_definition.html">zwplayer支持自适应码流</a>
    """
    return script     


@mcp.tool()
def zwplayer_autoplay() -> str:
    """zwplayer 自动播放"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
        <script type="text/javascript">
            // 定义一个js对象info ，用来做为ZWPlayer 的构造参数
            var videoObject = {
                playerElm: '#mse',
                autoplay: true,
                url: 'https://d2zihajmogu5jn.cloudfront.net/elephantsdream/ed_hd.mp4',

            };
            new ZWPlayer(videoObject);


        </script>
        
        demo: <a href="unit11_autoplay.html">zwplayer支持自动播放</a>
    """
    return script 
    

@mcp.tool()
def zwplayer_small_window() -> str:
    """zwplayer 窗口滚动将要隐藏播放器时，自动切换成弹出小窗口播放，缺省为false。有些产品页面比较大，有滚动条，当用户滚动页面时，会导致zwplayer被滚出页面之外而隐藏，如果将此参数设置为true，则在这种情况发生时，zwplayer自动切换成小窗口播放。注意：小窗口与画中画不一样，画中画是视频小窗口浮出在当前桌面的所有窗口的上面，而小窗口播放是视频小窗口仅在当前浏览器标签页内部，没有浮出。"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div style="height: 3000px;">
			<div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
		</div>
		<script type="text/javascript">
			// 定义一个js对象info ，用来做为ZWPlayer 的构造参数
			var videoObject = {
				playerElm: '#mse',
				autoplay: true,
				url: 'https://d2zihajmogu5jn.cloudfront.net/elephantsdream/ed_hd.mp4',
				autoSmallWindow: true,
			};
			new ZWPlayer(videoObject);
		</script>
        
        demo: <a href="unit12_smallWindows.html">zwplayer支持小窗口播放</a>
    """
    return script 
    
    
@mcp.tool()
def zwplayer_snapshot() -> str:
    """zwplayer 是否在播放控制条上显示图像截取按钮，缺省为false。点击图像截取按钮可以让用户一键截取当前正在播放的视频图像。"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
        <script type="text/javascript">
            // 定义一个js对象info ，用来做为ZWPlayer 的构造参数
            var videoObject = {
                playerElm: '#mse',
                autoplay: true,
                url: '//lf9-cdn-tos.bytecdntp.com/cdn/expire-1-M/byted-player-videos/1.0.0/xgplayer-demo.mp4',
                snapshotButton: true,
            };
            new ZWPlayer(videoObject);
        </script>
        
        demo: <a href="unit13_screenshot.html">zwplayer显示图像截取按钮</a>
    """
    return script  


@mcp.tool()
def zwplayer_seek() -> str:
    """zwplayer 定位播放时间，仅对点播节目有效。参数说明：time:要定位的时间，单位是秒，类型是浮点数。"""
    script = """
        <script type="text/javascript" charset="utf-8" src="./zwplayer/zwplayer.js"></script>
        <div class="video" id="mse" style="width: 1280px;height: 720px; margin: 0 auto;"></div>
		<script type="text/javascript">
			// 定义一个js对象info ，用来做为ZWPlayer 的构造参数
			var videoObject = {
				playerElm: '#mse',
				autoplay: true,
				url: 'https://d2zihajmogu5jn.cloudfront.net/elephantsdream/ed_hd.mp4',

			};
			var player = new ZWPlayer(videoObject);
			setTimeout(() => {
				// 这里放你要做的事
				player.seekTime(10);
			}, 500);
		</script>
        
        demo: <a href="unit14_lastPlayTime.html">zwplayer定位播放时间</a>
    """
    return script    


@mcp.resource("echo://static")
def echo_resource() -> str:
    return "Echo!"


@mcp.resource("echo://{text}")
def echo_template(text: str) -> str:
    """Echo the input text"""
    return f"Echo: {text}"


@mcp.prompt("echo")
def echo_prompt(text: str) -> str:
    return text


if __name__ == "__main__":
    # 默认参数: host="0.0.0.0", port=8000, path="/mcp"
    # mcp.run(transport="sse")
    
    # Run server with streamable_http transport
    mcp.run(transport="streamable-http")