<?php
include 'db_connection.php';

// Mendapatkan data fakultas dari URL
$fakultas = isset($_GET['fakultas']) ? $_GET['fakultas'] : 'FKIP';

// Query untuk mendapatkan data pengunjung berdasarkan fakultas
$sql = "SELECT bulan, jumlah_pengunjung FROM data_pengunjung WHERE fakultas = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param('s', $fakultas);
$stmt->execute();
$result = $stmt->get_result();

// Menampilkan data dalam tabel HTML
echo "<h2>Data Pengunjung Fakultas $fakultas</h2>";
echo "<table border='1'>";
echo "<tr><th>Bulan</th><th>Jumlah Pengunjung</th></tr>";
while ($row = $result->fetch_assoc()) {
    echo "<tr><td>" . $row['bulan'] . "</td><td>" . $row['jumlah_pengunjung'] . "</td></tr>";
}
echo "</table>";

$stmt->close();
$conn->close();
?>
