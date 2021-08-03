from flask import Flask
from flask_restful import Resource, Api, reqparse
from vk_app import profile, likes, posts

app = Flask(__name__)
api = Api(app)


class VK_APP(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'method',
            type=str,
            required=True,
            choices=('profile', 'likes', 'posts'),
            help='Bad choice: {error_msg}'
        )
        parser.add_argument('profile', type=str)
        parser.add_argument('link', type=str)
        parser.add_argument('posts', type=str)
        parser.add_argument('limit', type=int)

        args = parser.parse_args()

        # TODO переделать на dict мнонго if else
        if args.method == 'profile' and args.get('profile'):
            data = profile.get_data(args.profile)
            return {
                'status': 'success',
                'code': 200,
                'data': data
            }

        if args.method == 'likes' and args.get('link'):
            data = likes.get_data(args.link)
            return {
                'status': 'success',
                'code': 200,
                'data': data
            }

        if args.method == 'posts' and args.get('profile'):
            all_posts = []
            profile_data = profile.get_data(args.profile)
            if args.get('limit'):
                skip = 0
                while args.get('limit') > skip:
                    for post in posts.get_data(
                        alias=args.get('profile'),
                        skip=skip
                    ):
                        all_posts.append(post)
                    skip += 5
                profile_data['posts'] = all_posts[:args.get('limit')]
            else:
                for post in posts.get_data(alias=args.get('profile')):
                    all_posts.append(post)
                profile_data['posts'] = all_posts

            return {
                'status': 'success',
                'code': 200,
                'data': profile_data
            }
        return {
            'status': 'error',
            'code': 403,
            'message': 'Invalid account name'
        }


api.add_resource(VK_APP, '/api/v1')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
