import math

# 1. 'points' adında bir liste oluşturun
points = [(1, 2), (4, 6), (5, 10), (7, 2)]

# 2. Öklid mesafesi için bir fonksiyon tanımlayın
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# 3. Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Minimum mesafenin bulunması
min_distance = min(distances)

# Sonuçların yazdırılması
print("Tüm mesafeler:", distances)
print("Minimum mesafe:", min_distance)
