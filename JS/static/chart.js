document.addEventListener('DOMContentLoaded', () => {
    const fakultasSelect = document.getElementById('fakultas');
    const chartCtx = document.getElementById('chart').getContext('2d');
    let chart;

    fakultasSelect.addEventListener('change', async () => {
        const fakultas = fakultasSelect.value;
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ fakultas }),
        });
        const data = await response.json();

        // Update Chart
        if (chart) chart.destroy();
        const labels = data.frequent_itemsets.map(item => item.itemsets.join(", "));
        const support = data.frequent_itemsets.map(item => item.support);

        chart = new Chart(chartCtx, {
            type: 'bar',
            data: {
                labels,
                datasets: [{ label: 'Support', data: support }],
            },
        });

        // Update Table
        const tableBody = document.querySelector('#results-table tbody');
        tableBody.innerHTML = '';
        data.frequent_itemsets.forEach(item => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>${item.itemsets.join(", ")}</td><td>${item.support}</td>`;
            tableBody.appendChild(row);
        });
    });
});
