document.addEventListener('DOMContentLoaded', async function() {
    const token = localStorage.getItem('accessToken');
    if (!token) {
        window.location.href = '/login/';
        return;
    }

    // Logout Handler
    const logoutBtn = document.getElementById('logoutButton');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
            window.location.href = '/login/';
        });
    }

    // Dashboard Data Fetching
    if (document.getElementById('totalDisruptions')) {
        try {
            const response = await fetch('/api/disruption/user/', {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            
            if (!response.ok) throw new Error('Failed to fetch data');
            
            const disruptions = await response.json();
            updateStats(disruptions);
            renderCharts(disruptions);
        } catch (error) {
            console.error('Error:', error);
        }
    }
});

function updateStats(disruptions) {
    const total = disruptions.length;
    const downtime = disruptions.reduce((sum, d) => sum + d.duration, 0);
    const tags = new Set(disruptions.map(d => d.tag)).size;

    document.getElementById('totalDisruptions').textContent = total;
    document.getElementById('totalDowntime').textContent = `${downtime} min`;
    document.getElementById('uniqueTags').textContent = tags;

    // Avg per day
    if (total > 0) {
        const dates = new Set(disruptions.map(d => new Date(d.timestamp).toDateString()));
        const avg = (total / dates.size).toFixed(1);
        document.getElementById('avgDisruptionsPerDay').textContent = avg;
    }

    // Recent List
    const list = document.getElementById('recentDisruptionsList');
    list.innerHTML = '';
    
    if (total === 0) {
        list.innerHTML = '<p style="text-align: center; color: #777;">No recent disruptions.</p>';
        return;
    }

    disruptions.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp))
        .slice(0, 5)
        .forEach(d => {
            const item = document.createElement('div');
            item.className = 'disruption-item';
            item.innerHTML = `
                <h4>${d.tag_name || 'No Tag'} - ${new Date(d.timestamp).toLocaleString()}</h4>
                <p>Duration: ${d.duration} min | Severity: ${d.severity || 'N/A'}</p>
                ${d.root_cause_suggestion ? `<p style="color:#e0245e"><i class="fas fa-lightbulb"></i> ${d.root_cause_suggestion}</p>` : ''}
            `;
            list.appendChild(item);
        });
}

function renderCharts(disruptions) {
    // Tags Chart
    const tagCounts = {};
    disruptions.forEach(d => {
        const name = d.tag_name || 'Uncategorized';
        tagCounts[name] = (tagCounts[name] || 0) + 1;
    });

    new Chart(document.getElementById('tagsChart'), {
        type: 'doughnut',
        data: {
            labels: Object.keys(tagCounts),
            datasets: [{
                data: Object.values(tagCounts),
                backgroundColor: ['#4a90e2', '#50e3c2', '#f5a623', '#e0245e', '#9b59b6']
            }]
        },
        options: { plugins: { legend: { position: 'bottom' }, title: { display: true, text: 'By Tag' } } }
    });

    // Trend Chart
    const daily = {};
    disruptions.forEach(d => {
        const date = new Date(d.timestamp).toLocaleDateString();
        daily[date] = (daily[date] || 0) + 1;
    });
    
    const dates = Object.keys(daily).sort((a,b) => new Date(a) - new Date(b));

    new Chart(document.getElementById('trendChart'), {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: 'Daily Count',
                data: dates.map(d => daily[d]),
                borderColor: '#4a90e2',
                tension: 0.1
            }]
        },
        options: { plugins: { title: { display: true, text: 'Trend' } } }
    });
}
