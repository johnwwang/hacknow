<<<<<<< HEAD
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
    <heat-map
      :points="data"
      :lat="myCoordinates.lat"
      :lng="myCoordinates.lng"
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
      data: [
        { location: new google.maps.LatLng(37.782, -122.447), weight: 0.5 },
        new google.maps.LatLng(37.782, -122.445),
        { location: new google.maps.LatLng(37.782, -122.443), weight: 2 },
        { location: new google.maps.LatLng(37.782, -122.441), weight: 3 },
        { location: new google.maps.LatLng(37.782, -122.439), weight: 2 },
        new google.maps.LatLng(37.782, -122.437),
        { location: new google.maps.LatLng(37.782, -122.435), weight: 0.5 },

        { location: new google.maps.LatLng(37.785, -122.447), weight: 3 },
        { location: new google.maps.LatLng(37.785, -122.445), weight: 2 },
        new google.maps.LatLng(37.785, -122.443),
        { location: new google.maps.LatLng(37.785, -122.441), weight: 0.5 },
        new google.maps.LatLng(37.785, -122.439),
        { location: new google.maps.LatLng(37.785, -122.437), weight: 2 },
        { location: new google.maps.LatLng(37.785, -122.435), weight: 3 }
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