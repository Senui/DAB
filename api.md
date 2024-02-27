
# Data download flow (External Tool method)

1. User goes to portal.odissei.nl
2. User searches for a dataset
3. User goes to Access tab of dataset (containing an embedded version of the DAB)
4. The DAB receives the DOI from the odissei portal
5. The DAB resolves the DOI and retrieves the metadata
6. If the dataset is open access, the DAB fetches the download link (END)
7. If the dataset is restricted,  the DAB asks the user to login
8. User logs in with SURFConext
9. The DAB uses the Bearer Token from SURFConext to call the Dataverse Data Access API to check if the user has access to this DOI
10. If user has no access, show message: No Acccess (END)
11. If user has acces, DAB fetches the download link (END)

# Data download flow (Simple method)

1. User goes to portal.odissei.nl
2. User searches for a dataset
3. User goes to Access tab of dataset and clicks on DAB button
4. A new tab is opened with the DAB web interface
5. User fills in the DOI of the dataset of interest (can be skipped with the DOI forward query)
6. The DAB resolves the DOI and retrieves the metadata (including license)
7. If the dataset is open access, the DAB fetches the download link (END)
8. If the dataset is restricted,  the DAB asks the user to login
9. User logs in with SURFConext / SRAM
10. The DAB uses the Bearer Token from SURFConext to call the Dataverse Data Access API to check if the user has access to this DOI
    1.  Consent required from user for DAB as on-behalf service
11. If user has no access, show message: No Acccess (END)
12. If user has acces, DAB fetches the download link (END)

