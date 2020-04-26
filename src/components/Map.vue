<template>
  <div>
    <h1>hack::now</h1>
    <div style="display: flex; align-items: center; justify-content: space-between">
      <div>
        <h1>Your coordinates:</h1>
        <p>{{myCoordinates.lat.toFixed(4)}} Latitude, {{myCoordinates.lng.toFixed(4)}} Longitude</p>
      </div>
      <div>
        <h1>Map coordinates:</h1>
        <p>{{mapCoordinates.lat}} Latitude, {{mapCoordinates.lng}} Longitude</p>
      </div>
    </div>

    <GmapMap
      :center="myCoordinates"
      :zoom="7"
      style="width:640px; height: 360px; margin: 32px auto;"
      ref="mapRef"
      @dragend="handleDrag"
    ></GmapMap>
    <h2>1st</h2>
    <heat-map
      :points="data1"
      :lat="37.782"
      :lng="-122.447"
      style="width:640px; height: 360px; margin: 32px auto;"
    />
    <h2>2nd</h2>
    <heat-map
      :points="data2"
      :lat="37.782"
      :lng="-122.447"
      style="width:640px; height: 360px; margin: 32px auto;"
    />
    <h2>3rd</h2>
    <heat-map
      :points="data3"
      :lat="37.782"
      :lng="-122.447"
      style="width:640px; height: 360px; margin: 32px auto;"
    />
    <h2>4th</h2>
    <heat-map
      :points="data4"
      :lat="37.782"
      :lng="-122.447"
      style="width:640px; height: 360px; margin: 32px auto;"
    />
  </div>
</template>

<script>
import HeatMap from "@/components/HeatMap.vue";
export default {
  name: "view-page",
  components: { HeatMap },
  data() {
    return {
      map: null,
      myCoordinates: {
        lat: 0,
        lng: 0
      },
      zoom: 7,
      data1: [
        { location: new google.maps.LatLng(33, 65), weight: 1.835 },
        { location: new google.maps.LatLng(41.1533, 20.1683), weight: 0.679 },
        { location: new google.maps.LatLng(28.0339, 1.6596), weight: 0.92 },
        { location: new google.maps.LatLng(42.5063, 1.5218), weight: 1.848 },
        { location: new google.maps.LatLng(-8.830833, 13.245), weight: 0.007 },
        { location: new google.maps.LatLng(17.0608, -61.7964), weight: 0.771 },
        { location: new google.maps.LatLng(-38.4161, -63.6167), weight: 1.812 },
        { location: new google.maps.LatLng(40.0691, 45.0382), weight: 1.857 },
        { location: new google.maps.LatLng(47.5162, 14.5501), weight: 10.18 },
        { location: new google.maps.LatLng(40.1431, 47.5769), weight: 1.85 },
        {
          location: new google.maps.LatLng(25.066667, -77.333333),
          weight: 0.434
        },
        { location: new google.maps.LatLng(26.0275, 50.55), weight: 1.651 },
        { location: new google.maps.LatLng(23.685, 90.3563), weight: 0.423 },
        { location: new google.maps.LatLng(13.1939, -59.5432), weight: 0.23 },
        { location: new google.maps.LatLng(53.7098, 27.9534), weight: 0.232 },
        { location: new google.maps.LatLng(50.8333, 4), weight: 12.775 },
        {
          location: new google.maps.LatLng(17.498611, -88.188611),
          weight: 0.238
        },
        { location: new google.maps.LatLng(9.3077, 2.3158), weight: 0.507 },
        { location: new google.maps.LatLng(27.5142, 90.4336), weight: 0.813 },
        { location: new google.maps.LatLng(-16.2902, -63.5887), weight: 0.617 },
        { location: new google.maps.LatLng(43.9159, 17.6791), weight: 1.856 },
        {
          location: new google.maps.LatLng(-24.658056, 25.912222),
          weight: 0.084
        },
        { location: new google.maps.LatLng(-14.235, -51.9253), weight: 5.717 },
        { location: new google.maps.LatLng(4.5353, 114.7277), weight: 0.176 },
        { location: new google.maps.LatLng(42.7339, 25.4858), weight: 1.762 },
        { location: new google.maps.LatLng(12.2383, -1.5616), weight: 0.736 },
        { location: new google.maps.LatLng(16.85, 96.183333), weight: 0.52 },
        {
          location: new google.maps.LatLng(-3.383333, 29.366667),
          weight: 0.451
        },
        {
          location: new google.maps.LatLng(14.916667, -23.516667),
          weight: 0.045
        },
        { location: new google.maps.LatLng(11.55, 104.9167), weight: 0.2 },
        { location: new google.maps.LatLng(3.848, 11.5021), weight: 1.858 },
        { location: new google.maps.LatLng(56.1142, -106.344), weight: 45.783 },
        { location: new google.maps.LatLng(6.6111, 20.9394), weight: 0.404 },
        {
          location: new google.maps.LatLng(12.134722, 15.055833),
          weight: 0.472
        },
        { location: new google.maps.LatLng(-35.6751, -71.543), weight: 2.738 },
        { location: new google.maps.LatLng(35.9152, 104.2124), weight: 86.236 },
        { location: new google.maps.LatLng(4.5709, -74.2973), weight: 1.847 },
        { location: new google.maps.LatLng(-4.0383, 21.7587), weight: 0.882 },
        { location: new google.maps.LatLng(-4.0383, 21.7587), weight: 0.616 },
        { location: new google.maps.LatLng(9.7489, -83.7534), weight: 1.826 },
        { location: new google.maps.LatLng(45.1, 15.2), weight: 1.855 },
        { location: new google.maps.LatLng(22, -80), weight: 1.859 },
        { location: new google.maps.LatLng(35.1264, 33.4299), weight: 1.543 },
        { location: new google.maps.LatLng(49.8175, 15.473), weight: 3.308 },
        { location: new google.maps.LatLng(61.8926, -6.9118), weight: 2.86 },
        {
          location: new google.maps.LatLng(64.181389, -51.694167),
          weight: 2.86
        },
        { location: new google.maps.LatLng(56.2639, 9.5018), weight: 2.86 },
        { location: new google.maps.LatLng(35.4437, 139.638), weight: 1.341 },
        { location: new google.maps.LatLng(11.8251, 42.5903), weight: 1.186 },
        { location: new google.maps.LatLng(15.3, -61.383333), weight: 0.381 },
        { location: new google.maps.LatLng(18.7357, -70.1627), weight: 1.466 },
        { location: new google.maps.LatLng(-1.8312, -78.1834), weight: 2.24 },
        { location: new google.maps.LatLng(26, 30), weight: 0.917 },
        {
          location: new google.maps.LatLng(13.698889, -89.191389),
          weight: 1.252
        },
        { location: new google.maps.LatLng(1.5, 10), weight: 0.386 },
        { location: new google.maps.LatLng(15.322778, 38.925), weight: 0.786 },
        { location: new google.maps.LatLng(58.5953, 25.0136), weight: 1.849 },
        { location: new google.maps.LatLng(-26.5225, 31.4659), weight: 0.574 },
        { location: new google.maps.LatLng(9.145, 40.4897), weight: 0.878 },
        { location: new google.maps.LatLng(-18.166667, 178.45), weight: 0.316 },
        { location: new google.maps.LatLng(64, 26), weight: 1.847 },
        { location: new google.maps.LatLng(3.9339, -53.1258), weight: 52.128 },
        {
          location: new google.maps.LatLng(-17.6797, 149.4068),
          weight: 52.128
        },
        { location: new google.maps.LatLng(16.25, -61.5833), weight: 52.128 },
        { location: new google.maps.LatLng(14.666667, -61), weight: 52.128 },
        { location: new google.maps.LatLng(-12.8275, 45.1662), weight: 52.128 },
        { location: new google.maps.LatLng(-22.2758, 166.458), weight: 52.128 },
        { location: new google.maps.LatLng(-21.1351, 55.2471), weight: 52.128 },
        { location: new google.maps.LatLng(17.9, -62.8333), weight: 52.128 },
        { location: new google.maps.LatLng(46.7778, -56.1778), weight: 52.128 },
        { location: new google.maps.LatLng(18.0708, -63.0501), weight: 52.128 },
        { location: new google.maps.LatLng(46.2276, 2.2137), weight: 52.128 },
        { location: new google.maps.LatLng(-0.8037, 11.6094), weight: 0.976 },
        { location: new google.maps.LatLng(13.4432, -15.3101), weight: 0.068 },
        { location: new google.maps.LatLng(42.3154, 43.3569), weight: 0.187 },
        { location: new google.maps.LatLng(51, 9), weight: 71.808 },
        { location: new google.maps.LatLng(7.9465, -1.0232), weight: 1.859 },
        { location: new google.maps.LatLng(39.0742, 21.8243), weight: 1.58 },
        { location: new google.maps.LatLng(12.05, -61.75), weight: 0.376 },
        { location: new google.maps.LatLng(15.7835, -90.2308), weight: 0.287 },
        { location: new google.maps.LatLng(9.9456, -9.6966), weight: 1.224 },
        { location: new google.maps.LatLng(11.85, -15.566667), weight: 0.663 },
        { location: new google.maps.LatLng(5, -58.75), weight: 0.012 },
        {
          location: new google.maps.LatLng(18.533333, -72.333333),
          weight: 0.419
        },
        { location: new google.maps.LatLng(41.9029, 12.4534), weight: 0.889 },
        { location: new google.maps.LatLng(15.2, -86.2419), weight: 1.856 },
        { location: new google.maps.LatLng(47.1625, 19.5033), weight: 0.756 },
        { location: new google.maps.LatLng(64.9631, -19.0208), weight: 1.755 },
        { location: new google.maps.LatLng(21, 78), weight: 1.836 },
        { location: new google.maps.LatLng(-0.7893, 113.9213), weight: 1.528 },
        { location: new google.maps.LatLng(32, 53), weight: 44.605 },
        { location: new google.maps.LatLng(33, 44), weight: 0.957 },
        { location: new google.maps.LatLng(53.1424, -7.6921), weight: 3.235 },
        { location: new google.maps.LatLng(31, 35), weight: 5.358 },
        { location: new google.maps.LatLng(43, 12), weight: 105.792 },
        { location: new google.maps.LatLng(18.1096, -77.2975), weight: 0.232 },
        { location: new google.maps.LatLng(36, 138), weight: 1.953 },
        { location: new google.maps.LatLng(31.24, 36.51), weight: 1.813 },
        { location: new google.maps.LatLng(48.0196, 66.9237), weight: 1.856 },
        { location: new google.maps.LatLng(-0.0236, 37.9062), weight: 1.049 },
        { location: new google.maps.LatLng(36, 128), weight: 9.786 },
        {
          location: new google.maps.LatLng(42.666667, 21.166667),
          weight: 0.258
        },
        { location: new google.maps.LatLng(29.5, 47.75), weight: 0.289 },
        { location: new google.maps.LatLng(41.2044, 74.7661), weight: 1.149 },
        { location: new google.maps.LatLng(17.966667, 102.6), weight: 0.443 },
        { location: new google.maps.LatLng(56.8796, 24.6032), weight: 1.159 },
        { location: new google.maps.LatLng(33.8547, 35.8623), weight: 1.733 },
        { location: new google.maps.LatLng(6.4281, -9.4295), weight: 0.489 },
        {
          location: new google.maps.LatLng(32.887222, 13.191389),
          weight: 0.906
        },
        { location: new google.maps.LatLng(47.14, 9.55), weight: 0.17 },
        { location: new google.maps.LatLng(55.1694, 23.8813), weight: 1.853 },
        { location: new google.maps.LatLng(49.8153, 6.1296), weight: 2.178 },
        {
          location: new google.maps.LatLng(26.086111, -80.115278),
          weight: 0.275
        },
        {
          location: new google.maps.LatLng(-18.933333, 47.516667),
          weight: 1.111
        },
        {
          location: new google.maps.LatLng(-13.983333, 33.783333),
          weight: 0.0
        },
        { location: new google.maps.LatLng(2.5, 112.5), weight: 2.766 },
        { location: new google.maps.LatLng(3.2028, 73.2207), weight: 0.279 },
        {
          location: new google.maps.LatLng(12.639167, -8.002778),
          weight: 1.135
        },
        { location: new google.maps.LatLng(35.9375, 14.3754), weight: 0.253 },
        { location: new google.maps.LatLng(21.0079, 10.9408), weight: 0.161 },
        { location: new google.maps.LatLng(-20.2, 57.5), weight: 1.856 },
        { location: new google.maps.LatLng(23.6345, -102.5528), weight: 1.843 },
        { location: new google.maps.LatLng(47.4116, 28.3699), weight: 1.856 },
        { location: new google.maps.LatLng(43.7333, 7.4167), weight: 0.267 },
        { location: new google.maps.LatLng(46.8625, 103.8467), weight: 0.544 },
        { location: new google.maps.LatLng(42.5, 19.3), weight: 1.682 },
        { location: new google.maps.LatLng(31.7917, -7.0926), weight: 0.862 },
        {
          location: new google.maps.LatLng(-25.966667, 32.583333),
          weight: 0.345
        },
        { location: new google.maps.LatLng(-22.9576, 18.4904), weight: 0.84 },
        { location: new google.maps.LatLng(28.1667, 84.25), weight: 0.78 },
        { location: new google.maps.LatLng(12.5186, -70.0358), weight: 12.595 },
        {
          location: new google.maps.LatLng(12.144444, -68.265556),
          weight: 12.595
        },
        { location: new google.maps.LatLng(12.1696, -68.99), weight: 12.595 },
        {
          location: new google.maps.LatLng(18.052778, -63.0425),
          weight: 12.595
        },
        { location: new google.maps.LatLng(52.1326, 5.2913), weight: 12.595 },
        { location: new google.maps.LatLng(-40.9006, 174.886), weight: 1.853 },
        {
          location: new google.maps.LatLng(12.136389, -86.251389),
          weight: 0.011
        },
        {
          location: new google.maps.LatLng(13.511667, 2.125278),
          weight: 0.526
        },
        { location: new google.maps.LatLng(9.082, 8.6753), weight: 1.668 },
        { location: new google.maps.LatLng(41.6086, 21.7453), weight: 1.853 },
        { location: new google.maps.LatLng(60.472, 8.4689), weight: 4.641 },
        { location: new google.maps.LatLng(21, 57), weight: 1.024 },
        { location: new google.maps.LatLng(30.3753, 69.3451), weight: 1.938 },
        { location: new google.maps.LatLng(8.538, -80.7821), weight: 1.836 },
        {
          location: new google.maps.LatLng(-9.478889, 147.149444),
          weight: 0.259
        },
        { location: new google.maps.LatLng(-23.4425, -58.4438), weight: 1.858 },
        { location: new google.maps.LatLng(-9.19, -75.0152), weight: 1.791 },
        { location: new google.maps.LatLng(13, 122), weight: 2.084 },
        { location: new google.maps.LatLng(51.9194, 19.1451), weight: 2.311 },
        { location: new google.maps.LatLng(39.3999, -8.2245), weight: 7.443 },
        { location: new google.maps.LatLng(25.3548, 51.1839), weight: 1.358 },
        { location: new google.maps.LatLng(45.9432, 24.9668), weight: 2.245 },
        { location: new google.maps.LatLng(60, 90), weight: 2.337 },
        { location: new google.maps.LatLng(-1.9403, 29.8739), weight: 0.184 },
        { location: new google.maps.LatLng(17.3, -62.733333), weight: 0.779 },
        { location: new google.maps.LatLng(13.9094, -60.9789), weight: 1.224 },
        { location: new google.maps.LatLng(12.9843, -61.2872), weight: 0.609 },
        { location: new google.maps.LatLng(43.9424, 12.4578), weight: 0.822 },
        { location: new google.maps.LatLng(0.336111, 6.730556), weight: 0.0 },
        { location: new google.maps.LatLng(24, 45), weight: 1.856 },
        { location: new google.maps.LatLng(14.4974, -14.4524), weight: 0.36 },
        { location: new google.maps.LatLng(44.0165, 21.0059), weight: 1.851 },
        { location: new google.maps.LatLng(-4.6796, 55.492), weight: 0.865 },
        {
          location: new google.maps.LatLng(8.484444, -13.234444),
          weight: 0.28
        },
        { location: new google.maps.LatLng(1.2833, 103.8333), weight: 1.67 },
        { location: new google.maps.LatLng(48.669, 19.699), weight: 0.989 },
        { location: new google.maps.LatLng(46.1512, 14.9955), weight: 1.843 },
        { location: new google.maps.LatLng(5.1521, 46.1996), weight: 0.587 },
        { location: new google.maps.LatLng(-30.5595, 22.9375), weight: 1.857 },
        { location: new google.maps.LatLng(4.85, 31.6), weight: 0.0 },
        { location: new google.maps.LatLng(40, -4), weight: 95.923 },
        { location: new google.maps.LatLng(7, 81), weight: 0.246 },
        { location: new google.maps.LatLng(12.8628, 30.2176), weight: 0.008 },
        { location: new google.maps.LatLng(3.9193, -56.0278), weight: 0.573 },
        { location: new google.maps.LatLng(63, 16), weight: 4.435 },
        { location: new google.maps.LatLng(46.8182, 8.2275), weight: 16.605 },
        {
          location: new google.maps.LatLng(33.513056, 36.291944),
          weight: 0.01
        },
        { location: new google.maps.LatLng(23.7, 121), weight: 0.438 },
        { location: new google.maps.LatLng(-6.369, 34.8888), weight: 0.177 },
        { location: new google.maps.LatLng(15, 101), weight: 1.857 },
        {
          location: new google.maps.LatLng(-8.566667, 125.566667),
          weight: 0.185
        },
        { location: new google.maps.LatLng(8.6195, 0.8248), weight: 0.32 },
        { location: new google.maps.LatLng(10.6918, -61.2225), weight: 0.727 },
        { location: new google.maps.LatLng(34, 9), weight: 1.857 },
        { location: new google.maps.LatLng(38.9637, 35.2433), weight: 13.531 },
        {
          location: new google.maps.LatLng(0.313611, 32.581111),
          weight: 0.814
        },
        { location: new google.maps.LatLng(48.3794, 31.1656), weight: 1.852 },
        { location: new google.maps.LatLng(24, 54), weight: 1.856 },
        {
          location: new google.maps.LatLng(18.220833, -63.051667),
          weight: 25.15
        },
        { location: new google.maps.LatLng(32.293, -64.782), weight: 25.15 },
        {
          location: new google.maps.LatLng(18.431389, -64.623056),
          weight: 25.15
        },
        { location: new google.maps.LatLng(19.3133, -81.2546), weight: 25.15 },
        { location: new google.maps.LatLng(49.3723, -2.3644), weight: 25.15 },
        {
          location: new google.maps.LatLng(-51.694444, -57.852778),
          weight: 25.15
        },
        { location: new google.maps.LatLng(36.1408, -5.3536), weight: 25.15 },
        { location: new google.maps.LatLng(54.145, -4.482), weight: 25.15 },
        { location: new google.maps.LatLng(16.7425, -62.1874), weight: 25.15 },
        {
          location: new google.maps.LatLng(21.783333, -72.283333),
          weight: 25.15
        },
        { location: new google.maps.LatLng(55.3781, -3.436), weight: 25.15 },
        { location: new google.maps.LatLng(37.1358, -95.7845), weight: 95.673 },
        { location: new google.maps.LatLng(-32.5228, -55.7658), weight: 1.855 },
        { location: new google.maps.LatLng(41.3775, 64.5853), weight: 1.565 },
        { location: new google.maps.LatLng(6.4238, -66.5897), weight: 0.353 },
        { location: new google.maps.LatLng(16, 108), weight: 0.217 },
        {
          location: new google.maps.LatLng(31.703056, 35.195556),
          weight: 0.211
        },
        {
          location: new google.maps.LatLng(27.153611, -13.203333),
          weight: 0.0
        },
        { location: new google.maps.LatLng(-15.4167, 28.2833), weight: 0.327 },
        {
          location: new google.maps.LatLng(-17.829167, 31.052222),
          weight: 0.013
        }
      ],
      data2: [
        { location: new google.maps.LatLng(33, 65), weight: 2.039 },
        { location: new google.maps.LatLng(41.1533, 20.1683), weight: 0.953 },
        { location: new google.maps.LatLng(28.0339, 1.6596), weight: 1.012 },
        { location: new google.maps.LatLng(42.5063, 1.5218), weight: 2.032 },
        { location: new google.maps.LatLng(-8.830833, 13.245), weight: 0.007 },
        { location: new google.maps.LatLng(17.0608, -61.7964), weight: 1.379 },
        { location: new google.maps.LatLng(-38.4161, -63.6167), weight: 1.993 },
        { location: new google.maps.LatLng(40.0691, 45.0382), weight: 2.042 },
        { location: new google.maps.LatLng(47.5162, 14.5501), weight: 11.198 },
        { location: new google.maps.LatLng(40.1431, 47.5769), weight: 2.035 },
        {
          location: new google.maps.LatLng(25.066667, -77.333333),
          weight: 1.168
        },
        { location: new google.maps.LatLng(26.0275, 50.55), weight: 2.03 },
        { location: new google.maps.LatLng(23.685, 90.3563), weight: 0.631 },
        { location: new google.maps.LatLng(13.1939, -59.5432), weight: 0.253 },
        { location: new google.maps.LatLng(53.7098, 27.9534), weight: 0.255 },
        { location: new google.maps.LatLng(50.8333, 4), weight: 14.052 },
        {
          location: new google.maps.LatLng(17.498611, -88.188611),
          weight: 0.947
        },
        { location: new google.maps.LatLng(9.3077, 2.3158), weight: 1.337 },
        { location: new google.maps.LatLng(27.5142, 90.4336), weight: 1.424 },
        { location: new google.maps.LatLng(-16.2902, -63.5887), weight: 0.783 },
        { location: new google.maps.LatLng(43.9159, 17.6791), weight: 2.041 },
        {
          location: new google.maps.LatLng(-24.658056, 25.912222),
          weight: 0.238
        },
        { location: new google.maps.LatLng(-14.235, -51.9253), weight: 6.288 },
        { location: new google.maps.LatLng(4.5353, 114.7277), weight: 0.193 },
        { location: new google.maps.LatLng(42.7339, 25.4858), weight: 2.039 },
        { location: new google.maps.LatLng(12.2383, -1.5616), weight: 1.001 },
        { location: new google.maps.LatLng(16.85, 96.183333), weight: 1.314 },
        {
          location: new google.maps.LatLng(-3.383333, 29.366667),
          weight: 1.292
        },
        {
          location: new google.maps.LatLng(14.916667, -23.516667),
          weight: 0.27
        },
        { location: new google.maps.LatLng(11.55, 104.9167), weight: 0.22 },
        { location: new google.maps.LatLng(3.848, 11.5021), weight: 2.043 },
        { location: new google.maps.LatLng(56.1142, -106.344), weight: 51.423 },
        { location: new google.maps.LatLng(6.6111, 20.9394), weight: 1.437 },
        {
          location: new google.maps.LatLng(12.134722, 15.055833),
          weight: 1.278
        },
        { location: new google.maps.LatLng(-35.6751, -71.543), weight: 3.011 },
        { location: new google.maps.LatLng(35.9152, 104.2124), weight: 86.623 },
        { location: new google.maps.LatLng(4.5709, -74.2973), weight: 2.031 },
        { location: new google.maps.LatLng(-4.0383, 21.7587), weight: 1.24 },
        { location: new google.maps.LatLng(-4.0383, 21.7587), weight: 0.831 },
        { location: new google.maps.LatLng(9.7489, -83.7534), weight: 2.041 },
        { location: new google.maps.LatLng(45.1, 15.2), weight: 2.04 },
        { location: new google.maps.LatLng(22, -80), weight: 2.044 },
        { location: new google.maps.LatLng(35.1264, 33.4299), weight: 2.04 },
        { location: new google.maps.LatLng(49.8175, 15.473), weight: 3.638 },
        { location: new google.maps.LatLng(61.8926, -6.9118), weight: 3.146 },
        {
          location: new google.maps.LatLng(64.181389, -51.694167),
          weight: 3.146
        },
        { location: new google.maps.LatLng(56.2639, 9.5018), weight: 3.146 },
        { location: new google.maps.LatLng(35.4437, 139.638), weight: 1.558 },
        { location: new google.maps.LatLng(11.8251, 42.5903), weight: 1.304 },
        { location: new google.maps.LatLng(15.3, -61.383333), weight: 0.46 },
        { location: new google.maps.LatLng(18.7357, -70.1627), weight: 1.612 },
        { location: new google.maps.LatLng(-1.8312, -78.1834), weight: 2.464 },
        { location: new google.maps.LatLng(26, 30), weight: 1.008 },
        {
          location: new google.maps.LatLng(13.698889, -89.191389),
          weight: 1.401
        },
        { location: new google.maps.LatLng(1.5, 10), weight: 1.138 },
        { location: new google.maps.LatLng(15.322778, 38.925), weight: 1.237 },
        { location: new google.maps.LatLng(58.5953, 25.0136), weight: 2.035 },
        { location: new google.maps.LatLng(-26.5225, 31.4659), weight: 1.354 },
        { location: new google.maps.LatLng(9.145, 40.4897), weight: 1.203 },
        { location: new google.maps.LatLng(-18.166667, 178.45), weight: 1.322 },
        { location: new google.maps.LatLng(64, 26), weight: 2.031 },
        { location: new google.maps.LatLng(3.9339, -53.1258), weight: 57.34 },
        { location: new google.maps.LatLng(-17.6797, 149.4068), weight: 57.34 },
        { location: new google.maps.LatLng(16.25, -61.5833), weight: 57.34 },
        { location: new google.maps.LatLng(14.666667, -61), weight: 57.34 },
        { location: new google.maps.LatLng(-12.8275, 45.1662), weight: 57.34 },
        { location: new google.maps.LatLng(-22.2758, 166.458), weight: 57.34 },
        { location: new google.maps.LatLng(-21.1351, 55.2471), weight: 57.34 },
        { location: new google.maps.LatLng(17.9, -62.8333), weight: 57.34 },
        { location: new google.maps.LatLng(46.7778, -56.1778), weight: 57.34 },
        { location: new google.maps.LatLng(18.0708, -63.0501), weight: 57.34 },
        { location: new google.maps.LatLng(46.2276, 2.2137), weight: 57.34 },
        { location: new google.maps.LatLng(-0.8037, 11.6094), weight: 1.444 },
        { location: new google.maps.LatLng(13.4432, -15.3101), weight: 0.348 },
        { location: new google.maps.LatLng(42.3154, 43.3569), weight: 0.205 },
        { location: new google.maps.LatLng(51, 9), weight: 78.988 },
        { location: new google.maps.LatLng(7.9465, -1.0232), weight: 2.044 },
        { location: new google.maps.LatLng(39.0742, 21.8243), weight: 1.738 },
        { location: new google.maps.LatLng(12.05, -61.75), weight: 0.74 },
        { location: new google.maps.LatLng(15.7835, -90.2308), weight: 0.315 },
        { location: new google.maps.LatLng(9.9456, -9.6966), weight: 1.346 },
        { location: new google.maps.LatLng(11.85, -15.566667), weight: 1.273 },
        { location: new google.maps.LatLng(5, -58.75), weight: 0.013 },
        {
          location: new google.maps.LatLng(18.533333, -72.333333),
          weight: 0.83
        },
        { location: new google.maps.LatLng(41.9029, 12.4534), weight: 1.409 },
        { location: new google.maps.LatLng(15.2, -86.2419), weight: 2.041 },
        { location: new google.maps.LatLng(47.1625, 19.5033), weight: 0.997 },
        { location: new google.maps.LatLng(64.9631, -19.0208), weight: 2.027 },
        { location: new google.maps.LatLng(21, 78), weight: 2.019 },
        { location: new google.maps.LatLng(-0.7893, 113.9213), weight: 1.68 },
        { location: new google.maps.LatLng(32, 53), weight: 49.065 },
        { location: new google.maps.LatLng(33, 44), weight: 1.052 },
        { location: new google.maps.LatLng(53.1424, -7.6921), weight: 3.558 },
        { location: new google.maps.LatLng(31, 35), weight: 5.893 },
        { location: new google.maps.LatLng(43, 12), weight: 116.371 },
        { location: new google.maps.LatLng(18.1096, -77.2975), weight: 0.255 },
        { location: new google.maps.LatLng(36, 138), weight: 2.148 },
        { location: new google.maps.LatLng(31.24, 36.51), weight: 2.04 },
        { location: new google.maps.LatLng(48.0196, 66.9237), weight: 2.041 },
        { location: new google.maps.LatLng(-0.0236, 37.9062), weight: 1.243 },
        { location: new google.maps.LatLng(36, 128), weight: 10.764 },
        {
          location: new google.maps.LatLng(42.666667, 21.166667),
          weight: 0.283
        },
        { location: new google.maps.LatLng(29.5, 47.75), weight: 0.317 },
        { location: new google.maps.LatLng(41.2044, 74.7661), weight: 1.263 },
        { location: new google.maps.LatLng(17.966667, 102.6), weight: 1.177 },
        { location: new google.maps.LatLng(56.8796, 24.6032), weight: 1.274 },
        { location: new google.maps.LatLng(33.8547, 35.8623), weight: 2.032 },
        { location: new google.maps.LatLng(6.4281, -9.4295), weight: 1.423 },
        {
          location: new google.maps.LatLng(32.887222, 13.191389),
          weight: 1.285
        },
        { location: new google.maps.LatLng(47.14, 9.55), weight: 0.187 },
        { location: new google.maps.LatLng(55.1694, 23.8813), weight: 2.038 },
        { location: new google.maps.LatLng(49.8153, 6.1296), weight: 2.395 },
        {
          location: new google.maps.LatLng(26.086111, -80.115278),
          weight: 0.828
        },
        {
          location: new google.maps.LatLng(-18.933333, 47.516667),
          weight: 1.222
        },
        {
          location: new google.maps.LatLng(-13.983333, 33.783333),
          weight: 0.0
        },
        { location: new google.maps.LatLng(2.5, 112.5), weight: 3.042 },
        { location: new google.maps.LatLng(3.2028, 73.2207), weight: 0.306 },
        {
          location: new google.maps.LatLng(12.639167, -8.002778),
          weight: 1.36
        },
        { location: new google.maps.LatLng(35.9375, 14.3754), weight: 0.278 },
        { location: new google.maps.LatLng(21.0079, 10.9408), weight: 0.652 },
        { location: new google.maps.LatLng(-20.2, 57.5), weight: 2.041 },
        { location: new google.maps.LatLng(23.6345, -102.5528), weight: 2.027 },
        { location: new google.maps.LatLng(47.4116, 28.3699), weight: 2.041 },
        { location: new google.maps.LatLng(43.7333, 7.4167), weight: 0.293 },
        { location: new google.maps.LatLng(46.8625, 103.8467), weight: 1.254 },
        { location: new google.maps.LatLng(42.5, 19.3), weight: 2.04 },
        { location: new google.maps.LatLng(31.7917, -7.0926), weight: 1.012 },
        {
          location: new google.maps.LatLng(-25.966667, 32.583333),
          weight: 0.799
        },
        { location: new google.maps.LatLng(-22.9576, 18.4904), weight: 1.326 },
        { location: new google.maps.LatLng(28.1667, 84.25), weight: 1.411 },
        { location: new google.maps.LatLng(12.5186, -70.0358), weight: 13.854 },
        {
          location: new google.maps.LatLng(12.144444, -68.265556),
          weight: 13.854
        },
        { location: new google.maps.LatLng(12.1696, -68.99), weight: 13.854 },
        {
          location: new google.maps.LatLng(18.052778, -63.0425),
          weight: 13.854
        },
        { location: new google.maps.LatLng(52.1326, 5.2913), weight: 13.854 },
        { location: new google.maps.LatLng(-40.9006, 174.886), weight: 2.038 },
        {
          location: new google.maps.LatLng(12.136389, -86.251389),
          weight: 0.012
        },
        {
          location: new google.maps.LatLng(13.511667, 2.125278),
          weight: 0.676
        },
        { location: new google.maps.LatLng(9.082, 8.6753), weight: 2.042 },
        { location: new google.maps.LatLng(41.6086, 21.7453), weight: 2.038 },
        { location: new google.maps.LatLng(60.472, 8.4689), weight: 5.105 },
        { location: new google.maps.LatLng(21, 57), weight: 1.137 },
        { location: new google.maps.LatLng(30.3753, 69.3451), weight: 2.131 },
        { location: new google.maps.LatLng(8.538, -80.7821), weight: 2.019 },
        {
          location: new google.maps.LatLng(-9.478889, 147.149444),
          weight: 1.398
        },
        { location: new google.maps.LatLng(-23.4425, -58.4438), weight: 2.043 },
        { location: new google.maps.LatLng(-9.19, -75.0152), weight: 1.97 },
        { location: new google.maps.LatLng(13, 122), weight: 2.292 },
        { location: new google.maps.LatLng(51.9194, 19.1451), weight: 2.542 },
        { location: new google.maps.LatLng(39.3999, -8.2245), weight: 8.187 },
        { location: new google.maps.LatLng(25.3548, 51.1839), weight: 1.876 },
        { location: new google.maps.LatLng(45.9432, 24.9668), weight: 2.469 },
        { location: new google.maps.LatLng(60, 90), weight: 2.57 },
        { location: new google.maps.LatLng(-1.9403, 29.8739), weight: 0.202 },
        { location: new google.maps.LatLng(17.3, -62.733333), weight: 1.285 },
        { location: new google.maps.LatLng(13.9094, -60.9789), weight: 1.376 },
        { location: new google.maps.LatLng(12.9843, -61.2872), weight: 1.447 },
        { location: new google.maps.LatLng(43.9424, 12.4578), weight: 1.076 },
        { location: new google.maps.LatLng(0.336111, 6.730556), weight: 0.0 },
        { location: new google.maps.LatLng(24, 45), weight: 2.041 },
        { location: new google.maps.LatLng(14.4974, -14.4524), weight: 0.396 },
        { location: new google.maps.LatLng(44.0165, 21.0059), weight: 2.036 },
        { location: new google.maps.LatLng(-4.6796, 55.492), weight: 1.338 },
        {
          location: new google.maps.LatLng(8.484444, -13.234444),
          weight: 0.97
        },
        { location: new google.maps.LatLng(1.2833, 103.8333), weight: 2.026 },
        { location: new google.maps.LatLng(48.669, 19.699), weight: 1.087 },
        { location: new google.maps.LatLng(46.1512, 14.9955), weight: 2.027 },
        { location: new google.maps.LatLng(5.1521, 46.1996), weight: 1.399 },
        { location: new google.maps.LatLng(-30.5595, 22.9375), weight: 2.042 },
        { location: new google.maps.LatLng(4.85, 31.6), weight: 0.0 },
        { location: new google.maps.LatLng(40, -4), weight: 105.515 },
        { location: new google.maps.LatLng(7, 81), weight: 0.27 },
        { location: new google.maps.LatLng(12.8628, 30.2176), weight: 0.008 },
        { location: new google.maps.LatLng(3.9193, -56.0278), weight: 1.355 },
        { location: new google.maps.LatLng(63, 16), weight: 4.878 },
        { location: new google.maps.LatLng(46.8182, 8.2275), weight: 18.265 },
        {
          location: new google.maps.LatLng(33.513056, 36.291944),
          weight: 0.011
        },
        { location: new google.maps.LatLng(23.7, 121), weight: 0.51 },
        { location: new google.maps.LatLng(-6.369, 34.8888), weight: 0.238 },
        { location: new google.maps.LatLng(15, 101), weight: 2.042 },
        {
          location: new google.maps.LatLng(-8.566667, 125.566667),
          weight: 1.192
        },
        { location: new google.maps.LatLng(8.6195, 0.8248), weight: 0.352 },
        { location: new google.maps.LatLng(10.6918, -61.2225), weight: 1.505 },
        { location: new google.maps.LatLng(34, 9), weight: 2.042 },
        { location: new google.maps.LatLng(38.9637, 35.2433), weight: 14.884 },
        {
          location: new google.maps.LatLng(0.313611, 32.581111),
          weight: 1.153
        },
        { location: new google.maps.LatLng(48.3794, 31.1656), weight: 2.037 },
        { location: new google.maps.LatLng(24, 54), weight: 2.041 },
        {
          location: new google.maps.LatLng(18.220833, -63.051667),
          weight: 27.665
        },
        { location: new google.maps.LatLng(32.293, -64.782), weight: 27.665 },
        {
          location: new google.maps.LatLng(18.431389, -64.623056),
          weight: 27.665
        },
        { location: new google.maps.LatLng(19.3133, -81.2546), weight: 27.665 },
        { location: new google.maps.LatLng(49.3723, -2.3644), weight: 27.665 },
        {
          location: new google.maps.LatLng(-51.694444, -57.852778),
          weight: 27.665
        },
        { location: new google.maps.LatLng(36.1408, -5.3536), weight: 27.665 },
        { location: new google.maps.LatLng(54.145, -4.482), weight: 27.665 },
        { location: new google.maps.LatLng(16.7425, -62.1874), weight: 27.665 },
        {
          location: new google.maps.LatLng(21.783333, -72.283333),
          weight: 27.665
        },
        { location: new google.maps.LatLng(55.3781, -3.436), weight: 27.665 },
        {
          location: new google.maps.LatLng(37.1358, -95.7845),
          weight: 103.536
        },
        { location: new google.maps.LatLng(-32.5228, -55.7658), weight: 2.041 },
        { location: new google.maps.LatLng(41.3775, 64.5853), weight: 2.042 },
        { location: new google.maps.LatLng(6.4238, -66.5897), weight: 0.388 },
        { location: new google.maps.LatLng(16, 108), weight: 0.238 },
        {
          location: new google.maps.LatLng(31.703056, 35.195556),
          weight: 0.232
        },
        {
          location: new google.maps.LatLng(27.153611, -13.203333),
          weight: 0.0
        },
        { location: new google.maps.LatLng(-15.4167, 28.2833), weight: 0.359 },
        {
          location: new google.maps.LatLng(-17.829167, 31.052222),
          weight: 0.014
        }
      ],
      data3: [
        { location: new google.maps.LatLng(33, 65), weight: 2.132 },
        { location: new google.maps.LatLng(41.1533, 20.1683), weight: 1.033 },
        { location: new google.maps.LatLng(28.0339, 1.6596), weight: 1.058 },
        { location: new google.maps.LatLng(42.5063, 1.5218), weight: 2.125 },
        { location: new google.maps.LatLng(-8.830833, 13.245), weight: 0.008 },
        { location: new google.maps.LatLng(17.0608, -61.7964), weight: 1.442 },
        { location: new google.maps.LatLng(-38.4161, -63.6167), weight: 2.083 },
        { location: new google.maps.LatLng(40.0691, 45.0382), weight: 2.135 },
        { location: new google.maps.LatLng(47.5162, 14.5501), weight: 11.707 },
        { location: new google.maps.LatLng(40.1431, 47.5769), weight: 2.127 },
        {
          location: new google.maps.LatLng(25.066667, -77.333333),
          weight: 1.239
        },
        { location: new google.maps.LatLng(26.0275, 50.55), weight: 2.122 },
        { location: new google.maps.LatLng(23.685, 90.3563), weight: 1.417 },
        { location: new google.maps.LatLng(13.1939, -59.5432), weight: 0.264 },
        { location: new google.maps.LatLng(53.7098, 27.9534), weight: 0.266 },
        { location: new google.maps.LatLng(50.8333, 4), weight: 14.691 },
        {
          location: new google.maps.LatLng(17.498611, -88.188611),
          weight: 1.332
        },
        { location: new google.maps.LatLng(9.3077, 2.3158), weight: 1.398 },
        { location: new google.maps.LatLng(27.5142, 90.4336), weight: 1.489 },
        { location: new google.maps.LatLng(-16.2902, -63.5887), weight: 1.047 },
        { location: new google.maps.LatLng(43.9159, 17.6791), weight: 2.134 },
        {
          location: new google.maps.LatLng(-24.658056, 25.912222),
          weight: 0.286
        },
        { location: new google.maps.LatLng(-14.235, -51.9253), weight: 6.574 },
        { location: new google.maps.LatLng(4.5353, 114.7277), weight: 0.202 },
        { location: new google.maps.LatLng(42.7339, 25.4858), weight: 2.132 },
        { location: new google.maps.LatLng(12.2383, -1.5616), weight: 1.046 },
        { location: new google.maps.LatLng(16.85, 96.183333), weight: 1.374 },
        {
          location: new google.maps.LatLng(-3.383333, 29.366667),
          weight: 1.351
        },
        {
          location: new google.maps.LatLng(14.916667, -23.516667),
          weight: 1.104
        },
        { location: new google.maps.LatLng(11.55, 104.9167), weight: 0.229 },
        { location: new google.maps.LatLng(3.848, 11.5021), weight: 2.136 },
        { location: new google.maps.LatLng(56.1142, -106.344), weight: 52.474 },
        { location: new google.maps.LatLng(6.6111, 20.9394), weight: 1.503 },
        {
          location: new google.maps.LatLng(12.134722, 15.055833),
          weight: 1.336
        },
        { location: new google.maps.LatLng(-35.6751, -71.543), weight: 3.148 },
        { location: new google.maps.LatLng(35.9152, 104.2124), weight: 87.253 },
        { location: new google.maps.LatLng(4.5709, -74.2973), weight: 2.124 },
        { location: new google.maps.LatLng(-4.0383, 21.7587), weight: 1.297 },
        { location: new google.maps.LatLng(-4.0383, 21.7587), weight: 1.043 },
        { location: new google.maps.LatLng(9.7489, -83.7534), weight: 2.134 },
        { location: new google.maps.LatLng(45.1, 15.2), weight: 2.133 },
        { location: new google.maps.LatLng(22, -80), weight: 2.137 },
        { location: new google.maps.LatLng(35.1264, 33.4299), weight: 2.133 },
        { location: new google.maps.LatLng(49.8175, 15.473), weight: 3.804 },
        { location: new google.maps.LatLng(61.8926, -6.9118), weight: 3.288 },
        {
          location: new google.maps.LatLng(64.181389, -51.694167),
          weight: 3.288
        },
        { location: new google.maps.LatLng(56.2639, 9.5018), weight: 3.288 },
        { location: new google.maps.LatLng(35.4437, 139.638), weight: 2.113 },
        { location: new google.maps.LatLng(11.8251, 42.5903), weight: 1.363 },
        { location: new google.maps.LatLng(15.3, -61.383333), weight: 0.553 },
        { location: new google.maps.LatLng(18.7357, -70.1627), weight: 1.685 },
        { location: new google.maps.LatLng(-1.8312, -78.1834), weight: 2.576 },
        { location: new google.maps.LatLng(26, 30), weight: 1.054 },
        {
          location: new google.maps.LatLng(13.698889, -89.191389),
          weight: 1.465
        },
        { location: new google.maps.LatLng(1.5, 10), weight: 1.259 },
        { location: new google.maps.LatLng(15.322778, 38.925), weight: 1.293 },
        { location: new google.maps.LatLng(58.5953, 25.0136), weight: 2.127 },
        { location: new google.maps.LatLng(-26.5225, 31.4659), weight: 1.415 },
        { location: new google.maps.LatLng(9.145, 40.4897), weight: 1.258 },
        { location: new google.maps.LatLng(-18.166667, 178.45), weight: 1.414 },
        { location: new google.maps.LatLng(64, 26), weight: 2.124 },
        { location: new google.maps.LatLng(3.9339, -53.1258), weight: 59.947 },
        {
          location: new google.maps.LatLng(-17.6797, 149.4068),
          weight: 59.947
        },
        { location: new google.maps.LatLng(16.25, -61.5833), weight: 59.947 },
        { location: new google.maps.LatLng(14.666667, -61), weight: 59.947 },
        { location: new google.maps.LatLng(-12.8275, 45.1662), weight: 59.947 },
        { location: new google.maps.LatLng(-22.2758, 166.458), weight: 59.947 },
        { location: new google.maps.LatLng(-21.1351, 55.2471), weight: 59.947 },
        { location: new google.maps.LatLng(17.9, -62.8333), weight: 59.947 },
        { location: new google.maps.LatLng(46.7778, -56.1778), weight: 59.947 },
        { location: new google.maps.LatLng(18.0708, -63.0501), weight: 59.947 },
        { location: new google.maps.LatLng(46.2276, 2.2137), weight: 59.947 },
        { location: new google.maps.LatLng(-0.8037, 11.6094), weight: 1.509 },
        { location: new google.maps.LatLng(13.4432, -15.3101), weight: 1.339 },
        { location: new google.maps.LatLng(42.3154, 43.3569), weight: 0.215 },
        { location: new google.maps.LatLng(51, 9), weight: 82.579 },
        { location: new google.maps.LatLng(7.9465, -1.0232), weight: 2.137 },
        { location: new google.maps.LatLng(39.0742, 21.8243), weight: 1.816 },
        { location: new google.maps.LatLng(12.05, -61.75), weight: 1.162 },
        { location: new google.maps.LatLng(15.7835, -90.2308), weight: 0.33 },
        { location: new google.maps.LatLng(9.9456, -9.6966), weight: 1.407 },
        { location: new google.maps.LatLng(11.85, -15.566667), weight: 1.331 },
        { location: new google.maps.LatLng(5, -58.75), weight: 0.013 },
        {
          location: new google.maps.LatLng(18.533333, -72.333333),
          weight: 1.121
        },
        { location: new google.maps.LatLng(41.9029, 12.4534), weight: 1.473 },
        { location: new google.maps.LatLng(15.2, -86.2419), weight: 2.134 },
        { location: new google.maps.LatLng(47.1625, 19.5033), weight: 1.043 },
        { location: new google.maps.LatLng(64.9631, -19.0208), weight: 2.119 },
        { location: new google.maps.LatLng(21, 78), weight: 2.111 },
        { location: new google.maps.LatLng(-0.7893, 113.9213), weight: 1.757 },
        { location: new google.maps.LatLng(32, 53), weight: 51.295 },
        { location: new google.maps.LatLng(33, 44), weight: 1.1 },
        { location: new google.maps.LatLng(53.1424, -7.6921), weight: 3.72 },
        { location: new google.maps.LatLng(31, 35), weight: 6.161 },
        { location: new google.maps.LatLng(43, 12), weight: 121.66 },
        { location: new google.maps.LatLng(18.1096, -77.2975), weight: 0.266 },
        { location: new google.maps.LatLng(36, 138), weight: 2.245 },
        { location: new google.maps.LatLng(31.24, 36.51), weight: 2.133 },
        { location: new google.maps.LatLng(48.0196, 66.9237), weight: 2.134 },
        { location: new google.maps.LatLng(-0.0236, 37.9062), weight: 1.299 },
        { location: new google.maps.LatLng(36, 128), weight: 11.253 },
        {
          location: new google.maps.LatLng(42.666667, 21.166667),
          weight: 0.296
        },
        { location: new google.maps.LatLng(29.5, 47.75), weight: 0.332 },
        { location: new google.maps.LatLng(41.2044, 74.7661), weight: 1.321 },
        { location: new google.maps.LatLng(17.966667, 102.6), weight: 1.242 },
        { location: new google.maps.LatLng(56.8796, 24.6032), weight: 1.332 },
        { location: new google.maps.LatLng(33.8547, 35.8623), weight: 2.125 },
        { location: new google.maps.LatLng(6.4281, -9.4295), weight: 1.488 },
        {
          location: new google.maps.LatLng(32.887222, 13.191389),
          weight: 1.344
        },
        { location: new google.maps.LatLng(47.14, 9.55), weight: 0.195 },
        { location: new google.maps.LatLng(55.1694, 23.8813), weight: 2.13 },
        { location: new google.maps.LatLng(49.8153, 6.1296), weight: 2.504 },
        {
          location: new google.maps.LatLng(26.086111, -80.115278),
          weight: 1.266
        },
        {
          location: new google.maps.LatLng(-18.933333, 47.516667),
          weight: 1.277
        },
        {
          location: new google.maps.LatLng(-13.983333, 33.783333),
          weight: 0.0
        },
        { location: new google.maps.LatLng(2.5, 112.5), weight: 3.18 },
        { location: new google.maps.LatLng(3.2028, 73.2207), weight: 0.32 },
        {
          location: new google.maps.LatLng(12.639167, -8.002778),
          weight: 1.422
        },
        { location: new google.maps.LatLng(35.9375, 14.3754), weight: 0.29 },
        { location: new google.maps.LatLng(21.0079, 10.9408), weight: 1.477 },
        { location: new google.maps.LatLng(-20.2, 57.5), weight: 2.134 },
        { location: new google.maps.LatLng(23.6345, -102.5528), weight: 2.119 },
        { location: new google.maps.LatLng(47.4116, 28.3699), weight: 2.134 },
        { location: new google.maps.LatLng(43.7333, 7.4167), weight: 0.307 },
        { location: new google.maps.LatLng(46.8625, 103.8467), weight: 1.311 },
        { location: new google.maps.LatLng(42.5, 19.3), weight: 2.134 },
        { location: new google.maps.LatLng(31.7917, -7.0926), weight: 1.058 },
        {
          location: new google.maps.LatLng(-25.966667, 32.583333),
          weight: 1.207
        },
        { location: new google.maps.LatLng(-22.9576, 18.4904), weight: 1.386 },
        { location: new google.maps.LatLng(28.1667, 84.25), weight: 1.475 },
        { location: new google.maps.LatLng(12.5186, -70.0358), weight: 14.484 },
        {
          location: new google.maps.LatLng(12.144444, -68.265556),
          weight: 14.484
        },
        { location: new google.maps.LatLng(12.1696, -68.99), weight: 14.484 },
        {
          location: new google.maps.LatLng(18.052778, -63.0425),
          weight: 14.484
        },
        { location: new google.maps.LatLng(52.1326, 5.2913), weight: 14.484 },
        { location: new google.maps.LatLng(-40.9006, 174.886), weight: 2.13 },
        {
          location: new google.maps.LatLng(12.136389, -86.251389),
          weight: 0.012
        },
        {
          location: new google.maps.LatLng(13.511667, 2.125278),
          weight: 0.872
        },
        { location: new google.maps.LatLng(9.082, 8.6753), weight: 2.135 },
        { location: new google.maps.LatLng(41.6086, 21.7453), weight: 2.13 },
        { location: new google.maps.LatLng(60.472, 8.4689), weight: 5.337 },
        { location: new google.maps.LatLng(21, 57), weight: 1.189 },
        { location: new google.maps.LatLng(30.3753, 69.3451), weight: 2.228 },
        { location: new google.maps.LatLng(8.538, -80.7821), weight: 2.111 },
        {
          location: new google.maps.LatLng(-9.478889, 147.149444),
          weight: 1.505
        },
        { location: new google.maps.LatLng(-23.4425, -58.4438), weight: 2.136 },
        { location: new google.maps.LatLng(-9.19, -75.0152), weight: 2.059 },
        { location: new google.maps.LatLng(13, 122), weight: 2.396 },
        { location: new google.maps.LatLng(51.9194, 19.1451), weight: 2.657 },
        { location: new google.maps.LatLng(39.3999, -8.2245), weight: 8.559 },
        { location: new google.maps.LatLng(25.3548, 51.1839), weight: 2.119 },
        { location: new google.maps.LatLng(45.9432, 24.9668), weight: 2.581 },
        { location: new google.maps.LatLng(60, 90), weight: 2.687 },
        { location: new google.maps.LatLng(-1.9403, 29.8739), weight: 0.211 },
        { location: new google.maps.LatLng(17.3, -62.733333), weight: 1.344 },
        { location: new google.maps.LatLng(13.9094, -60.9789), weight: 1.438 },
        { location: new google.maps.LatLng(12.9843, -61.2872), weight: 1.513 },
        { location: new google.maps.LatLng(43.9424, 12.4578), weight: 1.125 },
        { location: new google.maps.LatLng(0.336111, 6.730556), weight: 0.0 },
        { location: new google.maps.LatLng(24, 45), weight: 2.134 },
        { location: new google.maps.LatLng(14.4974, -14.4524), weight: 0.413 },
        { location: new google.maps.LatLng(44.0165, 21.0059), weight: 2.128 },
        { location: new google.maps.LatLng(-4.6796, 55.492), weight: 1.399 },
        {
          location: new google.maps.LatLng(8.484444, -13.234444),
          weight: 1.291
        },
        { location: new google.maps.LatLng(1.2833, 103.8333), weight: 2.118 },
        { location: new google.maps.LatLng(48.669, 19.699), weight: 1.137 },
        { location: new google.maps.LatLng(46.1512, 14.9955), weight: 2.119 },
        { location: new google.maps.LatLng(5.1521, 46.1996), weight: 1.462 },
        { location: new google.maps.LatLng(-30.5595, 22.9375), weight: 2.135 },
        { location: new google.maps.LatLng(4.85, 31.6), weight: 0.0 },
        { location: new google.maps.LatLng(40, -4), weight: 110.311 },
        { location: new google.maps.LatLng(7, 81), weight: 0.282 },
        { location: new google.maps.LatLng(12.8628, 30.2176), weight: 0.009 },
        { location: new google.maps.LatLng(3.9193, -56.0278), weight: 1.416 },
        { location: new google.maps.LatLng(63, 16), weight: 5.1 },
        { location: new google.maps.LatLng(46.8182, 8.2275), weight: 19.095 },
        {
          location: new google.maps.LatLng(33.513056, 36.291944),
          weight: 0.011
        },
        { location: new google.maps.LatLng(23.7, 121), weight: 0.623 },
        { location: new google.maps.LatLng(-6.369, 34.8888), weight: 0.249 },
        { location: new google.maps.LatLng(15, 101), weight: 2.135 },
        {
          location: new google.maps.LatLng(-8.566667, 125.566667),
          weight: 1.505
        },
        { location: new google.maps.LatLng(8.6195, 0.8248), weight: 0.368 },
        { location: new google.maps.LatLng(10.6918, -61.2225), weight: 1.637 },
        { location: new google.maps.LatLng(34, 9), weight: 2.135 },
        { location: new google.maps.LatLng(38.9637, 35.2433), weight: 15.56 },
        {
          location: new google.maps.LatLng(0.313611, 32.581111),
          weight: 1.206
        },
        { location: new google.maps.LatLng(48.3794, 31.1656), weight: 2.129 },
        { location: new google.maps.LatLng(24, 54), weight: 2.134 },
        {
          location: new google.maps.LatLng(18.220833, -63.051667),
          weight: 28.922
        },
        { location: new google.maps.LatLng(32.293, -64.782), weight: 28.922 },
        {
          location: new google.maps.LatLng(18.431389, -64.623056),
          weight: 28.922
        },
        { location: new google.maps.LatLng(19.3133, -81.2546), weight: 28.922 },
        { location: new google.maps.LatLng(49.3723, -2.3644), weight: 28.922 },
        {
          location: new google.maps.LatLng(-51.694444, -57.852778),
          weight: 28.922
        },
        { location: new google.maps.LatLng(36.1408, -5.3536), weight: 28.922 },
        { location: new google.maps.LatLng(54.145, -4.482), weight: 28.922 },
        { location: new google.maps.LatLng(16.7425, -62.1874), weight: 28.922 },
        {
          location: new google.maps.LatLng(21.783333, -72.283333),
          weight: 28.922
        },
        { location: new google.maps.LatLng(55.3781, -3.436), weight: 28.922 },
        {
          location: new google.maps.LatLng(37.1358, -95.7845),
          weight: 104.463
        },
        { location: new google.maps.LatLng(-32.5228, -55.7658), weight: 2.134 },
        { location: new google.maps.LatLng(41.3775, 64.5853), weight: 2.135 },
        { location: new google.maps.LatLng(6.4238, -66.5897), weight: 0.405 },
        { location: new google.maps.LatLng(16, 108), weight: 0.249 },
        {
          location: new google.maps.LatLng(31.703056, 35.195556),
          weight: 0.242
        },
        {
          location: new google.maps.LatLng(27.153611, -13.203333),
          weight: 0.0
        },
        { location: new google.maps.LatLng(-15.4167, 28.2833), weight: 0.376 },
        {
          location: new google.maps.LatLng(-17.829167, 31.052222),
          weight: 0.014
        }
      ],
      data4: [
        { location: new google.maps.LatLng(33, 65), weight: 2.169 },
        { location: new google.maps.LatLng(41.1533, 20.1683), weight: 1.051 },
        { location: new google.maps.LatLng(28.0339, 1.6596), weight: 1.076 },
        { location: new google.maps.LatLng(42.5063, 1.5218), weight: 2.162 },
        { location: new google.maps.LatLng(-8.830833, 13.245), weight: 0.008 },
        { location: new google.maps.LatLng(17.0608, -61.7964), weight: 1.467 },
        { location: new google.maps.LatLng(-38.4161, -63.6167), weight: 2.12 },
        { location: new google.maps.LatLng(40.0691, 45.0382), weight: 2.172 },
        { location: new google.maps.LatLng(47.5162, 14.5501), weight: 11.91 },
        { location: new google.maps.LatLng(40.1431, 47.5769), weight: 2.164 },
        {
          location: new google.maps.LatLng(25.066667, -77.333333),
          weight: 1.261
        },
        { location: new google.maps.LatLng(26.0275, 50.55), weight: 2.159 },
        { location: new google.maps.LatLng(23.685, 90.3563), weight: 1.645 },
        { location: new google.maps.LatLng(13.1939, -59.5432), weight: 0.269 },
        { location: new google.maps.LatLng(53.7098, 27.9534), weight: 0.271 },
        { location: new google.maps.LatLng(50.8333, 4), weight: 14.946 },
        {
          location: new google.maps.LatLng(17.498611, -88.188611),
          weight: 1.356
        },
        { location: new google.maps.LatLng(9.3077, 2.3158), weight: 1.422 },
        { location: new google.maps.LatLng(27.5142, 90.4336), weight: 1.515 },
        { location: new google.maps.LatLng(-16.2902, -63.5887), weight: 1.065 },
        { location: new google.maps.LatLng(43.9159, 17.6791), weight: 2.171 },
        {
          location: new google.maps.LatLng(-24.658056, 25.912222),
          weight: 0.291
        },
        { location: new google.maps.LatLng(-14.235, -51.9253), weight: 6.688 },
        { location: new google.maps.LatLng(4.5353, 114.7277), weight: 0.205 },
        { location: new google.maps.LatLng(42.7339, 25.4858), weight: 2.169 },
        { location: new google.maps.LatLng(12.2383, -1.5616), weight: 1.064 },
        { location: new google.maps.LatLng(16.85, 96.183333), weight: 1.398 },
        {
          location: new google.maps.LatLng(-3.383333, 29.366667),
          weight: 1.374
        },
        {
          location: new google.maps.LatLng(14.916667, -23.516667),
          weight: 1.503
        },
        { location: new google.maps.LatLng(11.55, 104.9167), weight: 0.234 },
        { location: new google.maps.LatLng(3.848, 11.5021), weight: 2.173 },
        { location: new google.maps.LatLng(56.1142, -106.344), weight: 53.563 },
        { location: new google.maps.LatLng(6.6111, 20.9394), weight: 1.529 },
        {
          location: new google.maps.LatLng(12.134722, 15.055833),
          weight: 1.359
        },
        { location: new google.maps.LatLng(-35.6751, -71.543), weight: 3.203 },
        { location: new google.maps.LatLng(35.9152, 104.2124), weight: 88.153 },
        { location: new google.maps.LatLng(4.5709, -74.2973), weight: 2.16 },
        { location: new google.maps.LatLng(-4.0383, 21.7587), weight: 1.319 },
        { location: new google.maps.LatLng(-4.0383, 21.7587), weight: 1.061 },
        { location: new google.maps.LatLng(9.7489, -83.7534), weight: 2.171 },
        { location: new google.maps.LatLng(45.1, 15.2), weight: 2.17 },
        { location: new google.maps.LatLng(22, -80), weight: 2.175 },
        { location: new google.maps.LatLng(35.1264, 33.4299), weight: 2.17 },
        { location: new google.maps.LatLng(49.8175, 15.473), weight: 3.87 },
        { location: new google.maps.LatLng(61.8926, -6.9118), weight: 3.346 },
        {
          location: new google.maps.LatLng(64.181389, -51.694167),
          weight: 3.346
        },
        { location: new google.maps.LatLng(56.2639, 9.5018), weight: 3.346 },
        { location: new google.maps.LatLng(35.4437, 139.638), weight: 2.153 },
        { location: new google.maps.LatLng(11.8251, 42.5903), weight: 1.387 },
        { location: new google.maps.LatLng(15.3, -61.383333), weight: 1.026 },
        { location: new google.maps.LatLng(18.7357, -70.1627), weight: 1.715 },
        { location: new google.maps.LatLng(-1.8312, -78.1834), weight: 2.62 },
        { location: new google.maps.LatLng(26, 30), weight: 1.072 },
        {
          location: new google.maps.LatLng(13.698889, -89.191389),
          weight: 1.49
        },
        { location: new google.maps.LatLng(1.5, 10), weight: 1.281 },
        { location: new google.maps.LatLng(15.322778, 38.925), weight: 1.316 },
        { location: new google.maps.LatLng(58.5953, 25.0136), weight: 2.164 },
        { location: new google.maps.LatLng(-26.5225, 31.4659), weight: 1.44 },
        { location: new google.maps.LatLng(9.145, 40.4897), weight: 1.279 },
        { location: new google.maps.LatLng(-18.166667, 178.45), weight: 1.439 },
        { location: new google.maps.LatLng(64, 26), weight: 2.16 },
        { location: new google.maps.LatLng(3.9339, -53.1258), weight: 60.989 },
        {
          location: new google.maps.LatLng(-17.6797, 149.4068),
          weight: 60.989
        },
        { location: new google.maps.LatLng(16.25, -61.5833), weight: 60.989 },
        { location: new google.maps.LatLng(14.666667, -61), weight: 60.989 },
        { location: new google.maps.LatLng(-12.8275, 45.1662), weight: 60.989 },
        { location: new google.maps.LatLng(-22.2758, 166.458), weight: 60.989 },
        { location: new google.maps.LatLng(-21.1351, 55.2471), weight: 60.989 },
        { location: new google.maps.LatLng(17.9, -62.8333), weight: 60.989 },
        { location: new google.maps.LatLng(46.7778, -56.1778), weight: 60.989 },
        { location: new google.maps.LatLng(18.0708, -63.0501), weight: 60.989 },
        { location: new google.maps.LatLng(46.2276, 2.2137), weight: 60.989 },
        { location: new google.maps.LatLng(-0.8037, 11.6094), weight: 1.536 },
        { location: new google.maps.LatLng(13.4432, -15.3101), weight: 1.503 },
        { location: new google.maps.LatLng(42.3154, 43.3569), weight: 0.218 },
        { location: new google.maps.LatLng(51, 9), weight: 84.015 },
        { location: new google.maps.LatLng(7.9465, -1.0232), weight: 2.175 },
        { location: new google.maps.LatLng(39.0742, 21.8243), weight: 1.848 },
        { location: new google.maps.LatLng(12.05, -61.75), weight: 1.182 },
        { location: new google.maps.LatLng(15.7835, -90.2308), weight: 0.335 },
        { location: new google.maps.LatLng(9.9456, -9.6966), weight: 1.432 },
        { location: new google.maps.LatLng(11.85, -15.566667), weight: 1.354 },
        { location: new google.maps.LatLng(5, -58.75), weight: 0.014 },
        {
          location: new google.maps.LatLng(18.533333, -72.333333),
          weight: 1.14
        },
        { location: new google.maps.LatLng(41.9029, 12.4534), weight: 1.498 },
        { location: new google.maps.LatLng(15.2, -86.2419), weight: 2.171 },
        { location: new google.maps.LatLng(47.1625, 19.5033), weight: 1.061 },
        { location: new google.maps.LatLng(64.9631, -19.0208), weight: 2.156 },
        { location: new google.maps.LatLng(21, 78), weight: 2.148 },
        { location: new google.maps.LatLng(-0.7893, 113.9213), weight: 1.787 },
        { location: new google.maps.LatLng(32, 53), weight: 52.187 },
        { location: new google.maps.LatLng(33, 44), weight: 1.119 },
        { location: new google.maps.LatLng(53.1424, -7.6921), weight: 3.784 },
        { location: new google.maps.LatLng(31, 35), weight: 6.268 },
        { location: new google.maps.LatLng(43, 12), weight: 123.776 },
        { location: new google.maps.LatLng(18.1096, -77.2975), weight: 0.271 },
        { location: new google.maps.LatLng(36, 138), weight: 2.285 },
        { location: new google.maps.LatLng(31.24, 36.51), weight: 2.17 },
        { location: new google.maps.LatLng(48.0196, 66.9237), weight: 2.171 },
        { location: new google.maps.LatLng(-0.0236, 37.9062), weight: 1.322 },
        { location: new google.maps.LatLng(36, 128), weight: 11.449 },
        {
          location: new google.maps.LatLng(42.666667, 21.166667),
          weight: 0.301
        },
        { location: new google.maps.LatLng(29.5, 47.75), weight: 0.338 },
        { location: new google.maps.LatLng(41.2044, 74.7661), weight: 1.344 },
        { location: new google.maps.LatLng(17.966667, 102.6), weight: 1.263 },
        { location: new google.maps.LatLng(56.8796, 24.6032), weight: 1.356 },
        { location: new google.maps.LatLng(33.8547, 35.8623), weight: 2.162 },
        { location: new google.maps.LatLng(6.4281, -9.4295), weight: 1.513 },
        {
          location: new google.maps.LatLng(32.887222, 13.191389),
          weight: 1.367
        },
        { location: new google.maps.LatLng(47.14, 9.55), weight: 0.198 },
        { location: new google.maps.LatLng(55.1694, 23.8813), weight: 2.168 },
        { location: new google.maps.LatLng(49.8153, 6.1296), weight: 2.548 },
        {
          location: new google.maps.LatLng(26.086111, -80.115278),
          weight: 1.288
        },
        {
          location: new google.maps.LatLng(-18.933333, 47.516667),
          weight: 1.299
        },
        {
          location: new google.maps.LatLng(-13.983333, 33.783333),
          weight: 0.0
        },
        { location: new google.maps.LatLng(2.5, 112.5), weight: 3.236 },
        { location: new google.maps.LatLng(3.2028, 73.2207), weight: 0.326 },
        {
          location: new google.maps.LatLng(12.639167, -8.002778),
          weight: 1.447
        },
        { location: new google.maps.LatLng(35.9375, 14.3754), weight: 0.296 },
        { location: new google.maps.LatLng(21.0079, 10.9408), weight: 1.503 },
        { location: new google.maps.LatLng(-20.2, 57.5), weight: 2.171 },
        { location: new google.maps.LatLng(23.6345, -102.5528), weight: 2.156 },
        { location: new google.maps.LatLng(47.4116, 28.3699), weight: 2.171 },
        { location: new google.maps.LatLng(43.7333, 7.4167), weight: 0.312 },
        { location: new google.maps.LatLng(46.8625, 103.8467), weight: 1.333 },
        { location: new google.maps.LatLng(42.5, 19.3), weight: 2.171 },
        { location: new google.maps.LatLng(31.7917, -7.0926), weight: 1.076 },
        {
          location: new google.maps.LatLng(-25.966667, 32.583333),
          weight: 1.228
        },
        { location: new google.maps.LatLng(-22.9576, 18.4904), weight: 1.411 },
        { location: new google.maps.LatLng(28.1667, 84.25), weight: 1.501 },
        { location: new google.maps.LatLng(12.5186, -70.0358), weight: 14.736 },
        {
          location: new google.maps.LatLng(12.144444, -68.265556),
          weight: 14.736
        },
        { location: new google.maps.LatLng(12.1696, -68.99), weight: 14.736 },
        {
          location: new google.maps.LatLng(18.052778, -63.0425),
          weight: 14.736
        },
        { location: new google.maps.LatLng(52.1326, 5.2913), weight: 14.736 },
        { location: new google.maps.LatLng(-40.9006, 174.886), weight: 2.168 },
        {
          location: new google.maps.LatLng(12.136389, -86.251389),
          weight: 0.012
        },
        {
          location: new google.maps.LatLng(13.511667, 2.125278),
          weight: 1.061
        },
        { location: new google.maps.LatLng(9.082, 8.6753), weight: 2.172 },
        { location: new google.maps.LatLng(41.6086, 21.7453), weight: 2.168 },
        { location: new google.maps.LatLng(60.472, 8.4689), weight: 5.429 },
        { location: new google.maps.LatLng(21, 57), weight: 1.209 },
        { location: new google.maps.LatLng(30.3753, 69.3451), weight: 2.267 },
        { location: new google.maps.LatLng(8.538, -80.7821), weight: 2.148 },
        {
          location: new google.maps.LatLng(-9.478889, 147.149444),
          weight: 1.531
        },
        { location: new google.maps.LatLng(-23.4425, -58.4438), weight: 2.173 },
        { location: new google.maps.LatLng(-9.19, -75.0152), weight: 2.095 },
        { location: new google.maps.LatLng(13, 122), weight: 2.438 },
        { location: new google.maps.LatLng(51.9194, 19.1451), weight: 2.703 },
        { location: new google.maps.LatLng(39.3999, -8.2245), weight: 8.708 },
        { location: new google.maps.LatLng(25.3548, 51.1839), weight: 2.156 },
        { location: new google.maps.LatLng(45.9432, 24.9668), weight: 2.626 },
        { location: new google.maps.LatLng(60, 90), weight: 2.734 },
        { location: new google.maps.LatLng(-1.9403, 29.8739), weight: 0.215 },
        { location: new google.maps.LatLng(17.3, -62.733333), weight: 1.367 },
        { location: new google.maps.LatLng(13.9094, -60.9789), weight: 1.463 },
        { location: new google.maps.LatLng(12.9843, -61.2872), weight: 1.539 },
        { location: new google.maps.LatLng(43.9424, 12.4578), weight: 1.145 },
        { location: new google.maps.LatLng(0.336111, 6.730556), weight: 0.0 },
        { location: new google.maps.LatLng(24, 45), weight: 2.171 },
        { location: new google.maps.LatLng(14.4974, -14.4524), weight: 0.421 },
        { location: new google.maps.LatLng(44.0165, 21.0059), weight: 2.165 },
        { location: new google.maps.LatLng(-4.6796, 55.492), weight: 1.423 },
        {
          location: new google.maps.LatLng(8.484444, -13.234444),
          weight: 1.313
        },
        { location: new google.maps.LatLng(1.2833, 103.8333), weight: 2.155 },
        { location: new google.maps.LatLng(48.669, 19.699), weight: 1.157 },
        { location: new google.maps.LatLng(46.1512, 14.9955), weight: 2.156 },
        { location: new google.maps.LatLng(5.1521, 46.1996), weight: 1.488 },
        { location: new google.maps.LatLng(-30.5595, 22.9375), weight: 2.172 },
        { location: new google.maps.LatLng(4.85, 31.6), weight: 0.0 },
        { location: new google.maps.LatLng(40, -4), weight: 112.229 },
        { location: new google.maps.LatLng(7, 81), weight: 0.287 },
        { location: new google.maps.LatLng(12.8628, 30.2176), weight: 0.009 },
        { location: new google.maps.LatLng(3.9193, -56.0278), weight: 1.441 },
        { location: new google.maps.LatLng(63, 16), weight: 5.188 },
        { location: new google.maps.LatLng(46.8182, 8.2275), weight: 19.427 },
        {
          location: new google.maps.LatLng(33.513056, 36.291944),
          weight: 0.011
        },
        { location: new google.maps.LatLng(23.7, 121), weight: 1.198 },
        { location: new google.maps.LatLng(-6.369, 34.8888), weight: 0.253 },
        { location: new google.maps.LatLng(15, 101), weight: 2.172 },
        {
          location: new google.maps.LatLng(-8.566667, 125.566667),
          weight: 1.531
        },
        { location: new google.maps.LatLng(8.6195, 0.8248), weight: 0.374 },
        { location: new google.maps.LatLng(10.6918, -61.2225), weight: 2.156 },
        { location: new google.maps.LatLng(34, 9), weight: 2.172 },
        { location: new google.maps.LatLng(38.9637, 35.2433), weight: 15.831 },
        {
          location: new google.maps.LatLng(0.313611, 32.581111),
          weight: 1.227
        },
        { location: new google.maps.LatLng(48.3794, 31.1656), weight: 2.166 },
        { location: new google.maps.LatLng(24, 54), weight: 2.171 },
        {
          location: new google.maps.LatLng(18.220833, -63.051667),
          weight: 29.425
        },
        { location: new google.maps.LatLng(32.293, -64.782), weight: 29.425 },
        {
          location: new google.maps.LatLng(18.431389, -64.623056),
          weight: 29.425
        },
        { location: new google.maps.LatLng(19.3133, -81.2546), weight: 29.425 },
        { location: new google.maps.LatLng(49.3723, -2.3644), weight: 29.425 },
        {
          location: new google.maps.LatLng(-51.694444, -57.852778),
          weight: 29.425
        },
        { location: new google.maps.LatLng(36.1408, -5.3536), weight: 29.425 },
        { location: new google.maps.LatLng(54.145, -4.482), weight: 29.425 },
        { location: new google.maps.LatLng(16.7425, -62.1874), weight: 29.425 },
        {
          location: new google.maps.LatLng(21.783333, -72.283333),
          weight: 29.425
        },
        { location: new google.maps.LatLng(55.3781, -3.436), weight: 29.425 },
        {
          location: new google.maps.LatLng(37.1358, -95.7845),
          weight: 105.579
        },
        { location: new google.maps.LatLng(-32.5228, -55.7658), weight: 2.171 },
        { location: new google.maps.LatLng(41.3775, 64.5853), weight: 2.172 },
        { location: new google.maps.LatLng(6.4238, -66.5897), weight: 0.413 },
        { location: new google.maps.LatLng(16, 108), weight: 0.253 },
        {
          location: new google.maps.LatLng(31.703056, 35.195556),
          weight: 0.246
        },
        {
          location: new google.maps.LatLng(27.153611, -13.203333),
          weight: 0.0
        },
        { location: new google.maps.LatLng(-15.4167, 28.2833), weight: 0.382 },
        {
          location: new google.maps.LatLng(-17.829167, 31.052222),
          weight: 0.015
        }
        //saved
      ]
    };
  },

  created() {
    //does the user have saved center?
    if (localStorage.center) {
      this.myCoordinates = JSON.parse(localStorage.center);
    } else {
      //get user's coordinates from browser
      this.$getLocation({})
        .then(coordinates => {
          this.myCoordinates = coordinates;
        })
        .catch(error => alert(error));
    }
    //does zoom exist?
    if (localStorage.zoom) {
      this.zoom = parseInt(localStorage.zoom);
    } else {
      this.zoom = 7;
    }
  },

  mounted() {
    // add the map to a data object
    // fires after the component has loaded and attached to the vue instance
    //good for stuff that needs vue to be ready
    // this.$nextTick(() => {
    //   this.$refs.mapRef.$mapPromise.then(() => {
    //     var self = this;
    //     Http.post("v1/getheatmap").then(response => {
    //       let latlon = new google.maps.MVCArray();
    //       response.data.result.forEach(function(coord) {
    //         latlon.push(new google.maps.LatLng(coord.lat, coord.lng));
    //       });
    //       let x = new google.maps.visualization.HeatmapLayer({
    //         data: latlon,
    //         map: self.$refs.mymap.$mapObject
    //       });
    //     });
    //   });
    // });
    this.$refs.mapRef.$mapPromise.then(map => (this.map = map));
  },
  methods: {
    getCenterMap() {
      return {
        lat: this.data[this.data.length - 1].lat,
        lng: this.data[this.data.length - 1].lng
      };
    },
    handleDrag() {
      //get center and zoom level, store, and bring it back up
      let center = {
        lat: this.map.getCenter().lat(),
        lng: this.map.getCenter().lng()
      };
      let zoom = this.map.getZoom();
      localStorage.center = JSON.stringify(center);
      localStorage.zoom = zoom;
    }
  },
  computed: {
    mapCoordinates() {
      if (!this.map) {
        return {
          lat: 0,
          lng: 0
        };
      }
      return {
        lat: this.map
          .getCenter()
          .lat()
          .toFixed(4),
        lng: this.map
          .getCenter()
          .lng()
          .toFixed(4)
      };
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Vollkorn&display=swap");
* {
  font-family: "Vollkorn", serif;
}
</style>