from flask import Flask, render_template, request
import dif_search


app = Flask(__name__)

@app.route('/')
@app.route('/search')
def search_index():
    return render_template('search.html')

@app.route('/result', methods=['post'])
def result_index():
    if request.method == "POST":
        query_req = request.form.get('query')
        method_req = request.form.get('search_method')
        answer = dif_search.main(query_req, method_req)
    return render_template('result.html', query_req=query_req, answer=answer)



if __name__ == "__main__":
    app.run(debug=True)