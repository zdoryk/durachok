import { createStore } from 'vuex'
import actions from "./actions/actions";
import mutations from "./mutations/mutations";
import getters from "./getters/getters";
import apiRequests from './actions/api-requests'

const mapActions = {...actions, ...apiRequests}

let store = createStore({
    state: {
        card_values: {
            4: "4",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10",
            11: "jack",
            12: "queen",
            13: "king",
            14: "ace"
        },
        player: {
            player_state: 1,   // 1 - Attack, 2 - Defend, 3 - throw up ?
            is_player_active: true
        },
        table_size: 1200,
        kozir: {
            card_rank: 4, card_suit: "hearts", card_height: 150, card_index: 0
        },
        used_card_ranks: [6,7,8],

        cards: [
            {card_rank: 6, card_suit: "hearts", card_height: 120, card_index: 0},
            {card_rank: 8, card_suit: "spades", card_height: 120, card_index: 1},
            {card_rank: 9, card_suit: "hearts", card_height: 120, card_index: 2},
            {card_rank: 10, card_suit: "clubs", card_height: 120, card_index: 3},
            {card_rank: 14, card_suit: "hearts", card_height: 120, card_index: 4},
            {card_rank: 11, card_suit: "diamonds", card_height: 120, card_index: 5},
            {card_rank: 8, card_suit: "hearts", card_height: 120, card_index: 6},
            {card_rank: 9, card_suit: "spades", card_height: 120, card_index: 7},
            // {card_rank: 4, card_suit: "hearts", card_height: 15, card_index: 8},
            // {card_rank: 4, card_suit: "hearts", card_height: 15, card_index: 9},
            // {card_rank: 4, card_suit: "hearts", card_height: 15, card_index: 10},
            // {card_rank: 4, card_suit: "hearts", card_height: 15, card_index: 11},
            // {card_rank: 4, card_suit: "hearts", card_height: 15, card_index: 12},
            // {card_rank: 4, card_suit: "hearts", card_height: 15, card_index: 13},
            // {card_rank: 4, card_suit: "hearts", card_height: 15, card_index: 14},
            // {card_rank: 4, card_suit: "hearts", card_height: 15, card_index: 15},
        ],
        cards_on_bot: [
            {card_rank: 6, card_suit: "hearts", card_height: 120, card_index: 0},
            {card_rank: 7, card_suit: "hearts", card_height: 120, card_index: 1},
            {card_rank: 4, card_suit: "hearts", card_height: 120, card_index: 2},
            {card_rank: 4, card_suit: "hearts", card_height: 120, card_index: 3},
            {card_rank: 11, card_suit: "spades", card_height: 120, card_index: 4},
            {card_rank: 4, card_suit: "hearts", card_height: 120, card_index: 5},
            // {card_rank: 4, card_suit: "hearts", card_height: 120, card_index: 6},
        ],
        cards_on_top: [
            {card_rank: 8, card_suit: "hearts", card_height: 120, beaten: true, card_index: 0},
            {card_rank: 8, card_suit: "hearts", card_height: 120, beaten: false, card_index: 1},
            {card_rank: 6, card_suit: "hearts", card_height: 120, beaten: true, card_index: 2},
            {card_rank: 6, card_suit: "hearts", card_height: 120, beaten: true, card_index: 3},
            {card_rank: 8, card_suit: "hearts", card_height: 120, beaten: true, card_index: 4},
            {card_rank: 13, card_suit: "hearts", card_height: 120, beaten: true, card_index: 5},
            // {card_rank: 5, card_suit: "hearts", card_height: 120, beaten: true, card_index: 6},
        ]
    },
    mutations: mutations,
    actions: mapActions,
    getters: getters
});

export default store;
