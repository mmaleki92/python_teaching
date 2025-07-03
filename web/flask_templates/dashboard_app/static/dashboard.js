document.addEventListener('DOMContentLoaded', function() {
    // Initialize the dashboard
    updateDashboard();
    
    // Set up event listeners
    document.getElementById('refresh-btn').addEventListener('click', updateDashboard);
    document.getElementById('time-range').addEventListener('change', updateDashboard);
    document.getElementById('table-search').addEventListener('input', filterTable);
    document.getElementById('table-sort').addEventListener('change', sortTable);
    
    // Update timestamp
    document.getElementById('update-time').textContent = new Date().toLocaleString();
});

// Main dashboard update function
function updateDashboard() {
    fetchDashboardSummary();
    fetchProductData();
    fetchRegionData();
    fetchDailyTrend();
    
    // Update timestamp
    document.getElementById('update-time').textContent = new Date().toLocaleString();
}

// Fetch summary metrics
function fetchDashboardSummary() {
    fetch('/api/dashboard-summary')
        .then(response => response.json())
        .then(data => {
            // Update metric cards
            document.querySelector('#total-sales .metric-value').textContent = `$${numberWithCommas(data.total_sales)}`;
            document.querySelector('#total-units .metric-value').textContent = numberWithCommas(data.total_units);
            document.querySelector('#avg-order .metric-value').textContent = `$${data.avg_order_value.toFixed(2)}`;
            
            // Fake conversion rate (random between 2-5%)
            const conversionRate = (Math.random() * 3 + 2).toFixed(2);
            document.querySelector('#conversion .metric-value').textContent = `${conversionRate}%`;
            
            // Fake trend indicators (random between -10% and +15%)
            const metrics = document.querySelectorAll('.metric-card');
            metrics.forEach(metric => {
                const change = (Math.random() * 25 - 10).toFixed(1);
                const changeElement = metric.querySelector('.metric-change');
                
                changeElement.textContent = `${change >= 0 ? '+' : ''}${change}% from previous period`;
                changeElement.className = `metric-change ${change >= 0 ? 'positive' : 'negative'}`;
            });
        })
        .catch(error => console.error('Error fetching dashboard summary:', error));
}

// Fetch and render product data
function fetchProductData() {
    fetch('/api/sales-by-product')
        .then(response => response.json())
        .then(data => {
            renderProductChart(data);
            renderProductTable(data);
        })
        .catch(error => console.error('Error fetching product data:', error));
}

// Fetch and render region data
function fetchRegionData() {
    fetch('/api/sales-by-region')
        .then(response => response.json())
        .then(data => {
            renderRegionChart(data);
        })
        .catch(error => console.error('Error fetching region data:', error));
}

// Fetch and render daily trend data
function fetchDailyTrend() {
    fetch('/api/daily-trend')
        .then(response => response.json())
        .then(data => {
            renderTrendChart(data);
        })
        .catch(error => console.error('Error fetching daily trend:', error));
}

// Chart rendering functions
function renderProductChart(data) {
    const products = data.map(item => item.product);
    const sales = data.map(item => item.sales);
    
    const chartData = {
        labels: products,
        values: sales
    };
    
    Plotly.newPlot('product-chart', [{
        type: 'pie',
        labels: chartData.labels,
        values: chartData.values,
        textinfo: 'percent',
        hoverinfo: 'label+value',
        marker: {
            colors: ['#4361ee', '#3a0ca3', '#4cc9f0', '#f72585', '#7209b7']
        }
    }], {
        margin: { t: 0, r: 0, b: 0, l: 0 },
        height: 300,
        showlegend: true,
        legend: { orientation: 'h', y: -0.2 }
    });
}

function renderRegionChart(data) {
    const regions = data.map(item => item.region);
    const sales = data.map(item => item.sales);
    
    Plotly.newPlot('region-chart', [{
        type: 'bar',
        x: regions,
        y: sales,
        marker: {
            color: '#4361ee'
        }
    }], {
        margin: { t: 0, r: 20, b: 40, l: 60 },
        height: 300,
        xaxis: {
            title: 'Region'
        },
        yaxis: {
            title: 'Sales ($)'
        }
    });
}

function renderTrendChart(data) {
    const ctx = document.getElementById('trend-chart').getContext('2d');
    
    // Check if chart already exists and destroy
    if (window.trendChart) {
        window.trendChart.destroy();
    }
    
    window.trendChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map(item => item.date),
            datasets: [{
                label: 'Sales',
                data: data.map(item => item.sales),
                borderColor: '#4361ee',
                backgroundColor: 'rgba(67, 97, 238, 0.1)',
                borderWidth: 2,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `Sales: $${numberWithCommas(context.raw)}`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
}

// Table rendering and functionality
function renderProductTable(data) {
    const tableBody = document.querySelector('#product-table tbody');
    tableBody.innerHTML = '';
    
    data.forEach(item => {
        const row = document.createElement('tr');
        const avgPrice = (item.sales / item.units).toFixed(2);
        
        row.innerHTML = `
            <td>${item.product}</td>
            <td>$${numberWithCommas(item.sales.toFixed(2))}</td>
            <td>${numberWithCommas(item.units)}</td>
            <td>$${avgPrice}</td>
        `;
        
        tableBody.appendChild(row);
    });
    
    window.tableData = data; // Store data for filtering/sorting
}

function filterTable() {
    const searchTerm = document.getElementById('table-search').value.toLowerCase();
    const tableRows = document.querySelectorAll('#product-table tbody tr');
    
    tableRows.forEach(row => {
        const productName = row.cells[0].textContent.toLowerCase();
        row.style.display = productName.includes(searchTerm) ? '' : 'none';
    });
}

function sortTable() {
    const sortBy = document.getElementById('table-sort').value;
    const [field, direction] = sortBy.split('-');
    
    const sortedData = [...window.tableData].sort((a, b) => {
        let comparison = 0;
        
        if (field === 'sales') {
            comparison = a.sales - b.sales;
        } else if (field === 'units') {
            comparison = a.units - b.units;
        }
        
        return direction === 'asc' ? comparison : -comparison;
    });
    
    renderProductTable(sortedData);
}

// Utility functions
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}