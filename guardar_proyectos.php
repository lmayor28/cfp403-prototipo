<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Método no permitido']);
    exit;
}

$input = file_get_contents('php://input');
$data = json_decode($input, true);

if (!isset($data['pin']) || $data['pin'] !== '403') {
    http_response_code(401);
    echo json_encode(['error' => 'PIN de administrador no válido']);
    exit;
}

if (!isset($data['proyectos']) || !is_array($data['proyectos'])) {
    http_response_code(400);
    echo json_encode(['error' => 'Datos de proyectos no válidos']);
    exit;
}

$file = __DIR__ . '/proyectos.json';
if (file_put_contents($file, json_encode($data['proyectos'], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE))) {
    echo json_encode(['success' => true, 'mensaje' => 'Proyectos actualizados correctamente en el servidor']);
} else {
    http_response_code(500);
    echo json_encode(['error' => 'No se pudo escribir en el archivo proyectos.json en el servidor']);
}
