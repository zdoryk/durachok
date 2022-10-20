import { createStore } from 'vuex'
import commonActions from "./actions/mapActions";
import mutations from "./mutations/mutations";
import getters from "./getters/getters";
import apiRequests from './actions/api-requests'

const actions = {...commonActions, ...apiRequests}

let store = createStore({
    state: {

    },
    mutations: mutations,
    actions: actions,
    getters: getters
});

export default store;
