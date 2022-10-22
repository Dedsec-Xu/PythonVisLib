alert("请认真听讲！！");

// /**
//  * 新建图片对象
//  * @param url
//  * @returns {CanvasImage}
//  */
//     HTMLCanvasElement.prototype.newCanvasImage = function (url) {
//     if(!this.canvasImages) {
//         this.canvasImages = [];
//     }
//     var canvasImage = new CanvasImage(this, url);
//     this.canvasImages.push(canvasImage);
//     return canvasImage;
// };
// /**
//  * Canvas里面所有的图片
//  * @type {Array}
//  */
// HTMLCanvasElement.prototype.canvasImages = [];
// /**
//  * Canvas里面所有的图片
//  * @returns {Array}
//  */
// HTMLCanvasElement.prototype.getCanvasImage = function () {
//     if(!this.canvasImages) {
//     this.canvasImages = [];
//     }
//     return this.canvasImages;
// };

// /**
//  * Canvas图片对象
//  * @param canvas
//  * @param url 图片路径
//  * @constructor
//  */
// function CanvasImage(canvas, url) {
//     // 图片x坐标
//     CanvasImage.prototype.x;
//     // 图片y坐标
//     CanvasImage.prototype.y;
//     // 图片宽度
//     CanvasImage.prototype.width;
//     // 图片高度
//     CanvasImage.prototype.height;
//     // 图片对象
//     CanvasImage.prototype.image;
//     // 图片在Canva中原来的位置
//     CanvasImage.prototype.source;
//     // Canvas
//     CanvasImage.prototype.canvas;
//     CanvasImage.prototype.canvaContext;
//     // 是否显示
//     CanvasImage.prototype.isVisible;


//     this.image = new Image();
//     this.image.src = url;
//     this.x = 0;
//     this.y = 0;
//     this.width = 0;
//     this.height = 0;
//     this.source = null;
//     this.canvas = canvas;
//     this.canvaContext = canvas.getContext('2d');
//     this.isVisible = false;

//     /**
//      * 把图片移动到(x,y)
//      * @param x
//      * @param y
//      * @returns {boolean}
//      */
//     CanvasImage.prototype.moveTo = function(x,y) {
//         if(this.source) {
//             // 清理占用的位置
//             this.canvaContext.clearRect(this.x,this.y,this.width,this.height);
//             // 填充原位置的图像
//             this.canvaContext.putImageData(this.source,this.x,this.y);
//             // 设置新位置
//             this.x = x;
//             this.y = y;
//             // 获取新位置的图像
//             this.source = this.canvaContext.getImageData(this.x,this.y,this.width,this.height);
//             // 填充图片到新位置
//             this.canvaContext.drawImage(this.image,this.x,this.y,this.width,this.height);
//             return true;
//         } else {
//             return false;
//         }

//     };

//     /**
//      * 显示图片
//      * @param x
//      * @param y
//      * @returns {boolean}
//      */
//     CanvasImage.prototype.show = function(x,y) {
//         this.x = !!x ? x : this.x;
//         this.y = !!y ? y : this.y;
//         if(!!this.isVisible) {
//             return false;
//         } else {
//             this.isVisible = true;
//             // 获取占用位置的原图像
//             this.source = this.canvaContext.getImageData(this.x,this.y,this.width,this.height);
//             // 图片是否已经加载完成
//             if(this.image.complete) {
//                 // 加载完成，填充图片
//                 this.canvaContext.drawImage(this.image, this.x, this.y, this.width, this.height);
//             } else {
//                 // 没有加载完成，添加事件，待加载完成在填充图片
//                 this.canvaContext.onload = function(){
//                     // 填充图片
//                     this.canvaContext.drawImage(this.image, this.x, this.y, this.width, this.height);
//                 }
//             }
//             return true;
//         }
//     };

//     /**
//      * 隐藏图片
//      */
//     CanvasImage.prototype.hide = function() {
//         if(!!this.isVisible) {
//             this.isVisible = false;
//             // 清理占用的位置
//             this.canvaContext.clearRect(this.x,this.y,this.width,this.height);
//             // 填充原位置的图像
//             this.canvaContext.putImageData(this.source,this.x,this.y);
//         }
//     };

//     /**
//      * 设置图片大小
//      * @param w
//      * @param h
//      */
//     CanvasImage.prototype.setSize = function(w,h) {
//         this.width = w;
//         this.height = h;
//     };

//     CanvasImage.prototype.getSrc = function() {
//         return this.image.src;
//     };

//     /**
//      * 坐标是否在图片上
//      * @param x
//      * @param y
//      * @returns {boolean}
//      */
//     CanvasImage.prototype.isIn = function(x,y) {
//         if(x > this.x
//             && x < (this.x+this.width)
//             && y > this.y
//             && y < (this.y+this.height)
//         ){
//             return true;
//         }
//         return false;
//     };

//     CanvasImage.prototype.addMoveEvent = function(){
//         var th = this;
//         // 鼠标down事件
//         this.canvas.onmousedown=function (ev) {
//             // 只有图片显示时才执行mousedown事件。
//             if(!th.isVisible) {
//                 return;
//             }
//             // 记录mousedown时图片所在位置
//             var x = th.x;
//             var y = th.y;
//             // 判断鼠标是否在图片正上方
//             if(th.isIn(ev.layerX,ev.layerY)) {

//                 // 鼠标move事件
//                 this.onmousemove = function (e) {
//                     th.moveTo(x + e.layerX - ev.layerX,y + e.layerY - ev.layerY);
//                 };

//                 // 鼠标up事件
//                 this.onmouseup = function (e) {
//                     this.onmousemove = null;
//                     this.onmouseup = null;
//                 };
//             }
//         };
//     }
// }