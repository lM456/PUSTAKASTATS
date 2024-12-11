<?php
// Database connection
$servername = "localhost";
$username = "root";
$password = "";
$database = "pustakastats";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve POST data
$tahun = $_POST['tahun'];
$bulan = $_POST['bulan'];
$jumlah = $_POST['jumlah'];

// Prepare SQL query
$sql = "INSERT INTO peminjaman (tahun, bulan, jumlah) VALUES (?, ?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("isi", $tahun, $bulan, $jumlah);

if ($stmt->execute()) {
    echo "Data berhasil ditambahkan!";
} else {
    echo "Error: " . $conn->error;
}

$stmt->close();
$conn->close();
?>
