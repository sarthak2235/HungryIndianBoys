from flask import Flask, render_template, request
import os
# Get the current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the template folder path
template_folder = os.path.join(current_dir, 'template')

app = Flask(__name__, template_folder=template_folder)

# Rest of your Flask code...

restaurants = {
    1: {
        'name': 'Al Nawab',
        'location': 'Location 1',
        'contact': 'Contact 1',
        'photos': [
            'photos/AN1.jpg',
            'photos/AN2.jpg',
            'photos/AN3.jpg',
            'photos/AN3.jpg',
        ],
        'reviews': [
            {
                'user': 'Taste',
                'review': 'The food tastes good, but they need more staff and space. We waited over 45 minutes for the first meal. After requesting them multiple times, they served cold and chewy lamb chops. The curries were great in taste, but they were also cold. There is barely enough space to sit and move around. The plates and spoons were not very clean. Avoid going on weekends as it doesn\'t justify the price.'
            },
            {
                'user': 'Environment',
                'review': 'The food tastes good, but they need more staff and space. We waited over 45 minutes for the first meal. After requesting them multiple times, they served cold and chewy lamb chops. The curries were great in taste, but they were also cold. There is barely enough space to sit and move around. The plates and spoons were not very clean. Avoid going on weekends as it doesn\'t justify the price.'
            }
        ]
    },
    2: {
        'name': 'Desi Dhaba',
        'location': 'Location 1',
        'contact': 'Contact 1',
        'photos': [
            'photos/AN1.jpg',
            'photos/AN2.jpg',
            'photos/AN3.jpg',
            'photos/AN3.jpg',
        ],
        'reviews': [
            {
                'user': 'Taste',
                'review': 'The food tastes good, but they need more staff and space. We waited over 45 minutes for the first meal. After requesting them multiple times, they served cold and chewy lamb chops. The curries were great in taste, but they were also cold. There is barely enough space to sit and move around. The plates and spoons were not very clean. Avoid going on weekends as it doesn\'t justify the price.'
            },
            {
                'user': 'Environment',
                'review': 'The service here is excellent, and the staff is friendly.'
            }
        ]
    },
    3: {
        'name': 'Zyika',
        'location': 'Location 1',
        'contact': 'Contact 1',
        'photos': [
            'photos/AN1.jpg',
            'photos/AN2.jpg',
            'photos/AN3.jpg',
            'photos/AN3.jpg',
        ],
        'reviews': [
            {
                'user': 'Taste',
                'review': 'The food tastes good, but they need more staff and space. We waited over 45 minutes for the first meal. After requesting them multiple times, they served cold and chewy lamb chops. The curries were great in taste, but they were also cold. There is barely enough space to sit and move around. The plates and spoons were not very clean. Avoid going on weekends as it doesn\'t justify the price.'
            },
            {
                'user': 'Environment',
                'review': 'The service here is excellent, and the staff is friendly.'
            }
        ]
    },

    4: {
        'name': 'Zyika',
        'location': 'Location 1',
        'contact': 'Contact 1',
        'photos': [
            'photos/AN1.jpg',
            'photos/AN2.jpg',
            'photos/AN3.jpg',
            'photos/AN3.jpg',
        ],
        'reviews': [
            {
                'user': 'Taste',
                'review': 'The food tastes good, but they need more staff and space. We waited over 45 minutes for the first meal. After requesting them multiple times, they served cold and chewy lamb chops. The curries were great in taste, but they were also cold. There is barely enough space to sit and move around. The plates and spoons were not very clean. Avoid going on weekends as it doesn\'t justify the price.'
            },
            {
                'user': 'Environment',
                'review': 'The service here is excellent, and the staff is friendly.'
            }
        ]
    },

    5: {
        'name': 'Zyika',
        'location': 'Location 1',
        'contact': 'Contact 1',
        'photos': [
            'photos/AN1.jpg',
            'photos/AN2.jpg',
            'photos/AN3.jpg',
            'photos/AN3.jpg',
        ],
        'reviews': [
            {
                'user': 'Taste',
                'review': 'The food tastes good, but they need more staff and space. We waited over 45 minutes for the first meal. After requesting them multiple times, they served cold and chewy lamb chops. The curries were great in taste, but they were also cold. There is barely enough space to sit and move around. The plates and spoons were not very clean. Avoid going on weekends as it doesn\'t justify the price.'
            },
            {
                'user': 'Environment',
                'review': 'The service here is excellent, and the staff is friendly.'
            }
        ]
    },

    6: {
        'name': 'Zyika',
        'location': 'Location 1',
        'contact': 'Contact 1',
        'photos': [
            'photos/AN1.jpg',
            'photos/AN2.jpg',
            'photos/AN3.jpg',
            'photos/AN3.jpg',
        ],
        'reviews': [
            {
                'user': 'Taste',
                'review': 'The food tastes good, but they need more staff and space. We waited over 45 minutes for the first meal. After requesting them multiple times, they served cold and chewy lamb chops. The curries were great in taste, but they were also cold. There is barely enough space to sit and move around. The plates and spoons were not very clean. Avoid going on weekends as it doesn\'t justify the price.'
            },
            {
                'user': 'Environment',
                'review': 'The service here is excellent, and the staff is friendly.'
            }
        ]
    },

    # Add more restaurants as needed
}
##################################################################################################
##################################################################################################

@app.route('/')
def index():
    return render_template('index.html')

##################################################################################################

@app.route('/search')
def search():
    query = request.args.get('query')
    filtered_restaurants = []
    for restaurant_id, restaurant in restaurants.items():
        if query.lower() in restaurant['name'].lower():
            restaurant['id'] = restaurant_id  # Add the 'id' key to the restaurant dictionary
            filtered_restaurants.append(restaurant)
    return render_template('search.html', query=query, restaurants=filtered_restaurants)

##################################################################################################
@app.route('/restaurant/<int:restaurant_id>')
def restaurant(restaurant_id):
    restaurant = restaurants.get(restaurant_id)
    if restaurant:
        return render_template('restaurant.html', restaurant=restaurant)
    else:
        return "Restaurant not found."

if __name__ == '__main__':
    app.run(debug=True)
