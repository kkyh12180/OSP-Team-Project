<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>날름날음날씨와음식</title>
    <style>
        body{ padding:0px; margin:0px;}
        #divPosition{
            position:relative;
            height:300px;
            width:700px;
            margin:0px 0px 0px -290px;
            top:45%;
            left:50%;
            padding:5px;
        }
    </style>
    <script type = "text/javascript">
        function categoryChange(e) {
            var nam = ["대명동", "봉덕동", "이천동"];
            var dalseong = ["가창면", "구지면", "논공읍", "다사읍", "옥포읍", "유가읍", "하빈면", "현풍읍", "화원읍"];
            var dong = ["각산동", "검사동", "괴전동", "금강동", "내곡동", "내동", "능성동", "대림동", "덕곡동", "도동", "도학동", "동내동", "동호동", "둔산동", "매여동", "미곡동", "미대동", "방촌동", "백안동", "봉무동", "부동", "불로동", "사복동", "상매동", "서호동", "송정동", "숙천동", "신기동", "신무동", "신서동", "신암동", "신용동", "신천동", "신평동", "용계동", "용수동", "율암동", "율하동", "입석동", "중대동", "지묘동", "지저동", "진인동", "평광동", "효목동"];
            var buk = ["검단동", "고성동1가", "고성동2가", "고성동3가", "관음동", "구암동", "국우동", "금호동", "노곡동", "노원동1가", "노원동2가", "노원동3가", "대현동", "도남동", "동변동", "동천동", "동호동", "매천동", "복현동", "사수동", "산격동", "서변동", "연경동", "읍내동", "조야동", "칠성동1가", "칠성동2가", "침산동", "태전동", "팔달동", "학정동"]
            var nam = ["대명동", "봉덕동", "이천동"];
            var seo = ["내당동", "비산동", "상리동", "원대동1가", "원대동2가", "원대동3가", "이현동", "중리동", "평리동"];
            var suseong = ["가천동", "고모동", "노변동", "대흥동", "두산동", "만촌동", "매호동", "범물동", "범어동", "사월동", "삼덕동", "상동", "성동", "수성동1가", "수성동2가", "수성동3가", "수성동4가", "시지동", "신매동", "연호동", "욱수동", "이천동", "중동", "지산동", "파동", "황금동"];
            var jung = ["계산동1가", "계산동2가", "공평동", "교동", "남산동", "남성로", "남일동", "달성동", "대봉동", "대신동", "대안동", "덕산동", "도원동", "동문동", "동산동", "동성로1가", "동성로2가", "동성로3가", "동인동1가", "동인동2가", "동인동3가", "동인동4가", "동일동", "문화동", "봉산동", "북내동", "북성로1가", "북성로2가", "사일동", "삼덕동1가", "삼덕동2가", "삼덕동3가", "상덕동", "상서동", "서내동", "서문로1가", "서문로2가", "서성로1가", "서성로2가", "서야동", "수동", "수창동", "시장북로", "완전동", "용덕동", "인교동", "장관동", "전동", "종로1가", "종로2가", "태평로1가", "태평로2가", "태평로3가", "포정동", "하서동", "향촌동", "화전동"];
            var dalseo = ["갈산동", "감삼동", "대곡동", "대천동", "도원동", "두류동", "본동", "본리동", "상인동", "성당동", "송현동", "신당동", "용산동", "월성동", "월암동", "유천동", "이곡동", "장기동", "장동", "죽전동", "진천동", "파호동", "호림동", "호산동"]
            var target = document.getElementById("dong");
        
            if(e.value == "a") var d = nam;
            else if(e.value == "b") var d = dalseo;
            else if(e.value == "c") var d = dong;
            else if(e.value == "d") var d = buk;
            else if(e.value == "e") var d = seo;
            else if(e.value == "f") var d = suseong;
            else if(e.value == "g") var d = jung;
            else if(e.value == "h") var d = dalseong;
        
            target.options.length = 0;
        
            for (x in d) {
                var opt = document.createElement("option");
                opt.value = d[x];
                opt.innerHTML = d[x];
                target.appendChild(opt);
            }	
        }</script>
    </script>
  </head>
  <body>
    <div class="search">
        <center>
            <img src="{{url_for('static', filename='images/logo.png')}}" width="200" height="200">
        </center>
            
        <center>
            <h1>오늘 날씨엔 뭘 먹으면 좋을까?</h1>
            <h2>날름날름 사이트에 오신 것을 환영합니다!</h2>
        </center>
        <!-- </div>
        <div style="width:65%;height:200px;float: right;">
            <h1>오늘 날씨엔 뭘 먹으면 좋을까?</h1>
            <h2>날름날름 사이트에 오신 것을 환영합니다!</h2>
        </div> -->
	<form action = "/food" method = "POST">
		<br><br>
		<!-- <input type="search" name="keyword">
		<input type="submit" value="검쉑쉑"> -->
        <div id="divPosition">
            사용자님의 현위치를 설정해주세요!
            <select name = "gu" onchange="categoryChange(this)">
                <option>구를 선택해주세요</option>
                <option value="a">남구</option>
                <option value="b">달서구</option>
                <option value="c">동구</option>
                <option value="d">북구</option>
                <option value="e">서구</option>
                <option value="f">수성구</option>
                <option value="g">중구</option>
                <option value="h">달성구</option>
            </select>
            <select name = "dong" id="dong">
            <option>동/읍/면을 선택해주세요</option>
            </select>
            <input type="submit" value="전 여기 삽니다만..." class="input-btn">
        </div>
        </form>
    </div>
  </body>
</html>
