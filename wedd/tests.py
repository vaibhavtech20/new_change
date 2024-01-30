from django.test import TestCase

# Create your tests here.
#{% url 'send_interest' receiver_id=profile.id %}
#{% url 'shortlist' profile_id=profile.id %}
#{% url 'chat' receiver_id=profile.id %}

#      <!-- ... (previous code) ... -->

# <div class="profile-card">
#     <p>Name: {{ profile.name }}</p>
#     <p>Email: {{ profile.email }}</p>

#     <img src="{{ profile.profile_pic.url }}" alt="{{ profile.name }} Image" class="img-fluid mb-3">
#     <p>Name: {{ profile.name }}</p>
#     <p>Date of Birth: {{ profile.date_of_birth }}</p>
#     <!-- Add more profile details as needed -->

#     <!-- Action Buttons -->
#     <div class="action-buttons">
#         <form method="post" action="#"> 
             
#             {% csrf_token %}
#             <button type="submit" class="btn btn-primary">Send Interest</button>
#         </form>
        
#         <form method="post" action="#">
#             {% csrf_token %}
#             <button type="submit" class="btn btn-secondary">Shortlist</button>
#         </form>

#         <a href="#" class="btn btn-info">Chat</a>
#     </div>
# </div>

# <!-- ... (remaining code) ... -->


#        </div>
#     </div>