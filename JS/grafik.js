document.addEventListener("DOMContentLoaded", () => {
  const dataTable = document.querySelector("#dataTable tbody");
  const grafikContainer = document.getElementById("grafikContainer");
  const analisisText = document.getElementById("analisisText");

  // Analisis Data dan Tampilkan Grafik
  const btnAnalisis = document.getElementById("btnAnalisis");
  btnAnalisis.addEventListener("click", () => {
    const rows = Array.from(dataTable.rows);
    const data = rows.map(row => {
      const bulan = row.cells[0].textContent;
      const tahun = row.cells[1].textContent;
      const jumlah = parseInt(row.cells[2].textContent, 10);
      return { bulan, tahun, jumlah };
    });

    const labels = data.map(item => item.bulan);
    const jumlahPengunjung = data.map(item => item.jumlah);

    // Grafik Donat
    const donutCtx = document.getElementById("donutChart").getContext("2d");
    new Chart(donutCtx, {
      type: "doughnut",
      data: {
        labels,
        datasets: [{
          data: jumlahPengunjung,
          backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF", "#FF9F40"]
        }]
      }
    });

    // Grafik Batang
    const barCtx = document.getElementById("barChart").getContext("2d");
    new Chart(barCtx, {
      type: "bar",
      data: {
        labels,
        datasets: [{
          label: "Jumlah Pengunjung",
          data: jumlahPengunjung,
          backgroundColor: "#36A2EB"
        }]
      }
    });

    // Analisis
    const maxPengunjung = Math.max(...jumlahPengunjung);
    const bulanTertinggi = data[jumlahPengunjung.indexOf(maxPengunjung)].bulan;
    analisisText.textContent = `Bulan dengan pengunjung tertinggi adalah ${bulanTertinggi} dengan total ${maxPengunjung} pengunjung.`;

    grafikContainer.classList.remove("hidden");
  });
});
