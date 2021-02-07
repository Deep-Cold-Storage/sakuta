<template>
  <v-app>
    <!-- Responsive App Bar -->
    <v-app-bar app color="red accent-3" flat>
      <v-container class="py-1 fill-height">
        <v-icon large color="white" class="mx-2">mdi-book-account</v-icon>
        <h2 class="white--text font-weight-medium" v-show="$vuetify.breakpoint.mdAndUp">Sakuta's Dashboard</h2>

        <v-spacer></v-spacer>

        <v-responsive max-width="460" v-show="$vuetify.breakpoint.mdAndUp">
          <v-text-field
            dense
            flat
            hide-details
            solo
            rounded
            placeholder="Search Customers"
            prepend-inner-icon="mdi-account-search-outline"
            class="white"
            v-model="search"
          ></v-text-field>
        </v-responsive>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-4">
      <v-container>
        <v-row>
          <!-- Navigation -->
          <v-col xs="12" sm="12" md="12" lg="2">
            <v-sheet rounded>
              <v-list shaped rounded>
                <v-subheader>Navigation</v-subheader>

                <v-list-item-group>
                  <v-list-item>
                    <v-list-item-icon><v-icon>mdi-receipt</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Invocing</v-list-item-title></v-list-item-content>
                  </v-list-item>

                  <v-list-item>
                    <v-list-item-icon><v-icon>mdi-basket-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Orders</v-list-item-title></v-list-item-content>
                  </v-list-item>

                  <v-list-item>
                    <v-list-item-icon><v-icon>mdi-package-variant-closed</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Products</v-list-item-title></v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-sheet>
          </v-col>

          <!-- Main Table -->
          <v-col xs="12" sm="12" md="12" lg="7">
            <v-sheet rounded>
              <v-data-table
                :headers="headers"
                :items="customers"
                :search="search"
                disable-sort
                @click:row="handleTableClick"
                class="row-pointer"
                v-bind:loading="isLoading"
                loading-text="Gathering data..."
              >
                <template v-slot:[`item.name`]="{ item }">
                  <v-avatar size="40" class="ma-3" color="red accent-3" v-show="$vuetify.breakpoint.lgAndUp">
                    <span class="white--text text-h6">{{ getCustomerInitials(item.name) }}</span>
                  </v-avatar>

                  <span class="font-weight-medium ml-5">{{ item.name }}</span>
                </template>
              </v-data-table>
            </v-sheet>
          </v-col>

          <!-- Actions -->
          <v-col xs="12" sm="12" md="12" lg="2">
            <v-sheet rounded>
              <v-list rounded>
                <v-subheader>Actions</v-subheader>

                <v-list-item-group>
                  <v-list-item @click="$router.push('/customers/create')" color="red accent-3">
                    <v-list-item-icon><v-icon>mdi-account-plus-outline</v-icon></v-list-item-icon>
                    <v-list-item-content><v-list-item-title>Create Customer</v-list-item-title></v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    name: "Dashboard",
    data() {
      return {
        customers: [{ industry: "", nip: "", website: "" }],
        search: "",
        isLoading: true,

        headers: [
          {
            text: "Customer Name",
            align: "start",
            sortable: false,
            value: "name",
          },
          { text: "Industry", value: "industry" },
          { text: "NIP", value: "nip" },
          { text: "Website", value: "website" },
        ],
      };
    },
    methods: {
      getCustomers() {
        this.$http
          .get("/api/contractors")
          .then((response) => {
            this.customers = response.data;
            this.isLoading = false;
          })
          .catch((error) => {
            console.log(error);
          });
      },

      handleTableClick(row) {
        this.$router.push("/customers/" + row.contractor_id);

        console.log(row);
      },

      getCustomerInitials(name) {
        try {
          return name
            .split(" ")
            .map(function(item) {
              return item[0];
            })
            .join("")
            .substring(0, 2);
        } catch (error) {
          return "XD";
        }
      },
    },
    created() {
      this.getCustomers();
    },
  };
</script>

<style scoped>
  .row-pointer:hover {
    cursor: pointer;
  }
</style>
