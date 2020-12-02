jQuery(function ($) {
    $.supersized({
        slide_interval: 4000,
        transition: 1,
        transition_speed: 1000,
        performance: 1,
        min_width: 0,
        min_height: 0,
        vertical_center: 1,
        horizontal_center: 1,
        fit_always: 0,
        fit_portrait: 1,
        fit_landscape: 0,
        slide_links: 'blank',
        // slides: [{image: './images/1.jpg'}, {image: './images/2.jpg'}, {image: './images/3.jpg'}]
        slides: [{image: '/static/img/1.jpg'}, {image: '/static/img/2.jpg'}, {image: '/static/img/3.jpg'}]
        // 这里控制背景轮播图是js代码  这里必须用到相对路径  因为模板渲染已经完成了 最后才加载的js
    });
});