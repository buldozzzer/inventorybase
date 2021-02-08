<template>
  <div>
    <b-container>
      <b-col class="mt-3">
        <h3>Местоположения</h3>
      </b-col>
      <b-col>
        <b-button variant="success" class="mt-3" v-b-modal.location-add-modal>
          Добавить местопложение
        </b-button>
      </b-col>
      <location-table :locations="locations"
                      :edit-location="editLocation"
                      :select-to-remove-record="selectToRemoveLocation"/>
    </b-container>
    <location-add-modal/>
    <confirm-form :payload="selected[0]"
                  :dynamic-id="locationConfirm"
                  :message="locationMessage"
                  :op="removeLocation"/>
    <location-edit-modal ref="locationEdit"/>
  </div>
</template>

<script>
/* eslint-disable */
  import {bus} from "../../../main";
  import ConfirmForm from "../../item/ConfirmForm";
  import LocationTable from "../location/LocationTable";
  import LocationAddModal from "../location/LocationAddModal";
  import LocationEditModal from "../location/LocationEditModal";

  export default {
    name: 'EmployeePage',
    components: {
      ConfirmForm,
      LocationTable,
      LocationAddModal,
      LocationEditModal
    },
    data() {
      return {
        locationMessage: 'Удалить местоположение из базы?',
        locationConfirm: 'location-confirm',
        locations: [],
        selected: []
      };
    },
    methods: {
      async selectToRemoveLocation(data) {
        this.selected.push(data)
      },

      async fetchLocations() {
        const response = await fetch('http://localhost:8000/api/v1/location/')
        this.locations = await response.json()
        this.locations = this.locations['locations']
        this.selected = []
      },
      async removeLocation(unit) {
        const _id = unit['_id']
        const response = await fetch(`http://localhost:8000/api/v1/location/${_id}/`, {
          method: 'DELETE',
          headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
          },
        });
        if (response.status !== 204) {
          alert(JSON.stringify(await response.json(), null, 2));
        }
        await this.fetchLocations()
      },
      editLocation(item) {
        this.$refs.locationEdit.form = item
      },
    },
    async created() {
      await this.fetchLocations()

      await bus.$on('newData', () => {
        this.fetchLocations()
      })
    },
  };
</script>

<style scoped>

</style>
