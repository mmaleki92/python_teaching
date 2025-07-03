document.addEventListener('DOMContentLoaded', function() {
    // Load all charts
    loadStockChart();
    loadHistogramChart();
    loadPieChart();
});

// Stock chart with time series data
function loadStockChart() {
    fetch('/api/stock-data')
        .then(response => response.json())
        .then(data => {
            const trace = {
                x: data.dates,
                y: data.prices,
                type: 'scatter',
                mode: 'lines+markers',
                line: {
                    color: '#1da1f2',
                    width: 2
                },
                marker: {
                    size: 6,
                    color: '#1da1f2'
                },
                name: 'Stock Price'
            };
            
            const layout = {
                title: 'Stock Price Over Last 30 Days',
                xaxis: {
                    title: 'Date',
                    showgrid: false
                },
                yaxis: {
                    title: 'Price ($)',
                    showgrid: true,
                    gridcolor: '#f0f0f0'
                },
                margin: { t: 50, b: 50, l: 60, r: 20 },
                plot_bgcolor: 'rgba(0,0,0,0)',
                paper_bgcolor: 'rgba(0,0,0,0)'
            };
            
            Plotly.newPlot('stock-chart', [trace], layout, {responsive: true});
        })
        .catch(error => console.error('Error loading stock chart:', error));
    
    // Add control functionality
    document.getElementById('zoom-in').addEventListener('click', function() {
        const graph = document.getElementById('stock-chart');
        Plotly.relayout(graph, {
            'xaxis.range': [graph._fullLayout.xaxis.range[0] + 5, graph._fullLayout.xaxis.range[1] - 5]
        });
    });
    
    document.getElementById('zoom-out').addEventListener('click', function() {
        const graph = document.getElementById('stock-chart');
        Plotly.relayout(graph, {
            'xaxis.range': [graph._fullLayout.xaxis.range[0] - 5, graph._fullLayout.xaxis.range[1] + 5]
        });
    });
    
    document.getElementById('reset-view').addEventListener('click', function() {
        const graph = document.getElementById('stock-chart');
        Plotly.relayout(graph, {
            'xaxis.autorange': true,
            'yaxis.autorange': true
        });
    });
}

// Histogram chart
function loadHistogramChart() {
    fetch('/api/histogram-data')
        .then(response => response.json())
        .then(data => {
            const trace = {
                x: data.data,
                type: 'histogram',
                marker: {
                    color: '#36c',
                    line: {
                        color: 'white',
                        width: 1
                    }
                },
                opacity: 0.7
            };
            
            const layout = {
                title: 'Distribution of Values',
                xaxis: {
                    title: 'Value',
                },
                yaxis: {
                    title: 'Count',
                    gridcolor: '#f0f0f0'
                },
                margin: { t: 50, b: 50, l: 60, r: 20 },
                bargap: 0.05,
                plot_bgcolor: 'rgba(0,0,0,0)',
                paper_bgcolor: 'rgba(0,0,0,0)'
            };
            
            Plotly.newPlot('histogram-chart', [trace], layout, {responsive: true});
        })
        .catch(error => console.error('Error loading histogram chart:', error));
}

// Pie chart
function loadPieChart() {
    fetch('/api/pie-data')
        .then(response => response.json())
        .then(data => {
            const trace = {
                labels: data.categories,
                values: data.values,
                type: 'pie',
                marker: {
                    colors: ['#1da1f2', '#17bf63', '#794bc4', '#f45d22', '#ffad1f']
                },
                textinfo: 'percent',
                textposition: 'inside',
                hoverinfo: 'label+percent+value',
                hole: 0.4
            };
            
            const layout = {
                title: 'Category Distribution',
                margin: { t: 50, b: 20, l: 20, r: 20 },
                showlegend: true,
                legend: {
                    orientation: 'h',
                    y: -0.1
                },
                plot_bgcolor: 'rgba(0,0,0,0)',
                paper_bgcolor: 'rgba(0,0,0,0)'
            };
            
            Plotly.newPlot('pie-chart', [trace], layout, {responsive: true});
        })
        .catch(error => console.error('Error loading pie chart:', error));
}