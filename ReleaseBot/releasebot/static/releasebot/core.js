var Vue = require('vue');
var VueResource = require('vue-resource');
Vue.use(VueResource);
window.onload = function () {
    var main = new Vue({
        delimiters: ['[[', ']]'],
        el: '#app',
        data: function() {
            return {
                this.$http.get('/builds/', {params: {foo: 'bar'}}).then(response => {

                    // get body data
                    this.builds = response.body;

                  }, response => {
                    alert('server unavailable');
                  });
        };
        }
      });
}