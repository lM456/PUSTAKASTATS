<?php
include 'db_connection.php';

$fakultas = isset($_GET['fakultas']) ? $_GET['fakultas'] : 'FKIP';

$sql = "SELECT bulan, jumlah_pengunjung FROM data_pengunjung WHERE fakultas = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param('s', $fakultas);
$stmt->execute();
$result = $stmt->get_result();

$data = [];
while ($row = $result->fetch_assoc()) {
    $data[] = $row;
}
echo json_encode($data);

$stmt->close();
$conn->close();
?>
