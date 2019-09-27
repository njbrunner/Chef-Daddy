<template>
    <div class="form-row">
        <div class="col-7">
            <input type="text" class="form-control" placeholder="Name" v-model="name">
        </div>
        <div class="col-2">
            <input type="text" class="form-control" placeholder="Quantity" v-model="quantity">
        </div>
        <div class="col-2">
            <input type="text" class="form-control" placeholder="Measurement" v-model="measurement">
        </div>
        <button class="col-1 btn btn-outline-success" @click="addIngredient"><i class="fas fa-plus"></i></button>
    </div>
</template>
<script>
export default {
    name: 'IngredientForm',
    data() {
        return {
            name: null,
            quantity: null,
            measurement: null
        }
    },
    methods: {
        addIngredient() {
            var data = {
                'name': this.name,
                'quantity': this.quantity,
                'measurement': this.measurement
            }
            this.$emit('addIngredient', data);
        }
    },
}
</script>
<style scoped>
.form-control {
    width: 100%;
    margin: 0;
}
.expand {
    width: 100%;
}
</style>
