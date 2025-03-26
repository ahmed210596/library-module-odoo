odoo.define('library_module.dashboard', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var ajax = require('web.ajax');
    var QWeb = core.qweb;

    var LibraryDashboard = AbstractAction.extend({
        template: 'library_module.LibraryDashboardTemplate',
        events: {},
        
        init: function(parent, action) {
            this._super.apply(this, arguments);
            this.stats = {
                total_books: 0,
                borrowed_books: 0,
                available_books: 0
            };
            this.chart = null;
        },
        
        start: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                return self._loadStats();
            });
        },
        
        _loadStats: function () {
            var self = this;
            return ajax.jsonRpc("/library/dashboard/stats", "call", {})
                .then(function(result) {
                    self.stats = result;
                    self._renderChart();
                });
        },
        
        _renderChart: function () {
            if (this.chart) {
                this.chart.destroy();
            }
            var ctx = this.el.querySelector('#myChart').getContext('2d');
            this.chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Total', 'Borrowed', 'Available'],
                    datasets: [{
                        label: 'Books',
                        data: [this.stats.total_books, this.stats.borrowed_books, this.stats.available_books],
                        backgroundColor: ['blue', 'red', 'green'],
                    }]
                }
            });
        },
        
        destroy: function() {
            if (this.chart) {
                this.chart.destroy();
            }
            this._super.apply(this, arguments);
        }
    });

    core.action_registry.add('library_dashboard', LibraryDashboard);

    return LibraryDashboard;
});