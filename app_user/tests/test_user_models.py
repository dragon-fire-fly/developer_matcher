# # perform an initial count
# initial_count = User.objects.count()

# # create a new user object
# User.objects.create() # ?
# # and then compare the count after account creation
# self.assertEqual(User.objects.count(), initial_count+1)
# # and/or that the exact oject has been created
# User.objects.get(username="")
# # test if something exists
# self.assertTrue(User.objects.filter(id=).exists)

# # or check if the user exists (does it raise a DoesNotExist error)
# self.assertRaises(User.DoesNotExist, User.objects.get, id=self.user.id)


# for the form, can test the submission is successful
