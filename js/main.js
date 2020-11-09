

var localserver = "http://127.0.0.1:8000/api/getjson?query=";

// 日本地図の描画
var drawJapanMap = function(){
    //d3.json(localserver+"japan.topojson", function(error, japanmap) {
    d3.json("data/master_data/japan.topojson", function(error, japanmap) {
        // 基本設定
        var width = 800;
        var height = 700;
        var scale = 1400;
        var svg = d3.select(".japanmap")
            .attr("width", width)
            .attr("height", height);
        // topojsonからgeojsonオブジェクトを生成
        var prefs = topojson.object(japanmap, japanmap.objects.japan);
        // 投影方法
        var projection = d3.geoMercator()
            .scale(scale)
            .translate( [width / 2, height / 2])
            .center([139.44,35.39]);
        // svgのパス要素
        var path = d3.geoPath()
            .projection( projection );
        // 各国のパスを作成
        var map = svg.selectAll(".prefs")
            .data(prefs.geometries)
            .enter()
            .append("path")
            .attr("class", function(d) { return "pref " + d.properties.id; } )
            .attr("d", path)
            .style("fill", function(d){return rand_color();} );
    
        // ズームイベント
        var zoom = d3.zoom().on('zoom', function(){
            projection.scale(scale * d3.event.transform.k);
            map.attr('d',path);
        });
        svg.call(zoom);
        // ドラッグイベント
        var drag = d3.drag().on('drag', function(){
            var tl = projection.translate();
            projection.translate([tl[0] + d3.event.dx, tl[1] + d3.event.dy]);
            map.attr('d',path);
        });
        map.call(drag);
    
    });
    // 県別に描画できてるかテスト
    function rand_color(){
        var r = Math.floor( Math.random() * 255 ).toString(16);
        var g = Math.floor( Math.random() * 255 ).toString(16);
        var b = Math.floor( Math.random() * 255 ).toString(16);
        return "#" + r + g + b;
    }
}

var main = function(){
    drawJapanMap();
}();