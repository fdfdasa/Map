// Kiểm tra xem trình duyệt có hỗ trợ geolocation không
var vietnamBounds = [
    [8.1790665, 102.14441], // Tây Nam
    [23.393395, 109.4646833]  // Đông Bắc
];

// Tạo bản đồ và giới hạn trong khu vực Việt Nam
var map = L.map('map', {
    center: [16.047079, 108.206230], // Trung tâm ban đầu ở Việt Nam
    zoom: 6,
    minZoom: 5,
    maxZoom: 18,
    maxBounds: vietnamBounds,
    maxBoundsViscosity: 1.0
});

L.tileLayer('https://api.maptiler.com/maps/streets-v2/{z}/{x}/{y}.png?key=JQQlTlGt6mgmsQLj7Hrr', {
    attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>',
    tileSize: 512, 
    zoomOffset: -1, 
    minZoom: 5,
    maxZoom: 18
}).addTo(map);

// Kiểm tra và lấy vị trí hiện tại của người dùng
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;

        // Lưu vị trí vào Local Storage
        localStorage.setItem('userLatitude', latitude);
        localStorage.setItem('userLongitude', longitude);
        
        console.log('Vị trí của bạn đã được lưu:', latitude, longitude);

        var userCoords = [latitude, longitude];

        // Thêm marker tại vị trí của người dùng
        L.marker(userCoords).addTo(map)
            .bindPopup('Đây là vị trí của bạn.')
            .openPopup();
        
        map.setView(userCoords, 13);

    }, function(error) {
        console.error('Lỗi khi lấy vị trí của người dùng:', error);
        alert('Không thể lấy vị trí của bạn. Vui lòng kiểm tra cài đặt vị trí của trình duyệt.');
    });
} else {
    console.log('Trình duyệt của bạn không hỗ trợ geolocation.');
}

// Xử lý sự kiện cho bong bóng tìm kiếm nổi
document.querySelector('#floating-search input').addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        console.log('Tìm kiếm trên bản đồ:', this.value);

        fetch('http://127.0.0.1:5000/direction', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: this.value })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Kết quả tìm kiếm:', data);

            var name = data.name;
            var address = data.address;
            var latitude = data.coordinates[0];
            var longitude = data.coordinates[1];

            var hospitalCoords = [latitude, longitude];

            L.marker(hospitalCoords).addTo(map)
                .bindPopup('<b>'+name+'</b><br>'+address)
                .openPopup();

            calculateAndDisplayRoute(hospitalCoords);
        })
        .catch(error => {
            console.error('Lỗi khi tìm kiếm:', error);
            alert('Không thể thực hiện tìm kiếm. Vui lòng thử lại sau.');
        });
    }
});

// Khởi tạo tọa độ của người dùng từ Local Storage
var userCoords = [
    parseFloat(localStorage.getItem('userLatitude')),
    parseFloat(localStorage.getItem('userLongitude'))
];

function calculateAndDisplayRoute(hospitalCoords) {
    // Xóa tuyến đường cũ nếu có
    if (window.routeLayer) {
        map.removeLayer(window.routeLayer);
    }

    // Kiểm tra xem userCoords có hợp lệ không
    if (!userCoords[0] || !userCoords[1]) {
        console.error('Vị trí của người dùng không hợp lệ.');
        alert('Vui lòng cấp quyền truy cập vị trí của bạn để tính toán tuyến đường.');
        return;
    }

    // Gọi API OSRM
    fetch(`https://router.project-osrm.org/route/v1/driving/${userCoords[1]},${userCoords[0]};${hospitalCoords[1]},${hospitalCoords[0]}?overview=full&geometries=geojson`)
        .then(response => response.json())
        .then(data => {
            if (data.routes && data.routes.length > 0) {
                const route = data.routes[0];
                const distance = route.distance / 1000; // Chuyển đổi từ mét sang km
                const duration = Math.round(route.duration / 60); // Chuyển đổi từ giây sang phút

                // Hiển thị thông tin khoảng cách và thời gian
                document.getElementById('distance').innerHTML = `Khoảng cách theo tuyến đường là: ${distance.toFixed(2)} km, mất khoảng: ${duration} phút.`;

                // Hiển thị tuyến đường trên bản đồ
                window.routeLayer = L.geoJSON(route.geometry).addTo(map);
                map.fitBounds(window.routeLayer.getBounds());
            } else {
                alert('Không có tuyến đường nào được tìm thấy.');
            }
        })
        .catch(error => {
            console.error('Lỗi:', error);
            alert('Không thể tính toán tuyến đường. Vui lòng thử lại sau.');
        });
}
