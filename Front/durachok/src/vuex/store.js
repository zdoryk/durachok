import { createStore } from 'vuex'
import commonActions from "./actions/mapActions";
import mutations from "./mutations/mutations";
import getters from "./getters/getters";
import apiRequests from './actions/api-requests'

const actions = {...commonActions, ...apiRequests}

let store = createStore({
    state: {
        card: {
            card_rank: '5',
            card_suit: 'hearts',
            card_path: "../assets/cards/SVG-cards-1.3/5_of_hearts.svg"
        }
    },
    mutations: mutations,
    actions: actions,
    getters: getters
});

export default store;
