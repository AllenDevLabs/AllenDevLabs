CREATE TABLE service_logs (
  id INTEGER PRIMARY KEY,
  client TEXT NOT NULL,
  service TEXT NOT NULL,
  status TEXT NOT NULL
);

INSERT INTO service_logs (client, service, status) VALUES
('Ava', 'PC repair', 'Complete'),
('Noah', 'Smart TV setup', 'Pending');

SELECT client, service, status FROM service_logs ORDER BY id;
