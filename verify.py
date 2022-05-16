# Import the client library
import google.cloud.dlp
from csv import reader, writer
from criptografar import encrypt_symmetric

# Instantiate a client.
dlp_client = google.cloud.dlp_v2.DlpServiceClient()

# The string to inspect
info_types = [{"name": "EMAIL_ADDRESS"}]

min_likelihood = google.cloud.dlp_v2.Likelihood.LIKELIHOOD_UNSPECIFIED

max_findings = 0

include_quote = True

inspect_config = {
    "info_types": info_types,
    "min_likelihood": min_likelihood,
    "include_quote": include_quote,
    "limits": {"max_findings_per_request": max_findings},
}

project_id = "bix-tecnologia-dev"

# Convert the project id into a full resource id.
parent = f"projects/{project_id}"

with open('/home/lucas_franca/py-dlp/python-dlp/codificado.csv', 'w') as write_obj:
    writer = writer(write_obj)
    with open('/home/lucas_franca/py-dlp/python-dlp/teste.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        # Iterate over each row in the csv using reader object
        if header != None:
            for row in csv_reader:
                new_row = []
                # row variable is a list that represents a row in csv
                for element in row:
                    item = {"value": element}

                    response = dlp_client.inspect_content(
                        request={"parent": parent, "inspect_config": inspect_config, "item": item}
                    )

                    # Print out the results.
                    if response.result.findings:
                        for finding in response.result.findings:
                            try:
                                print("Quote: {}".format(finding.quote))
                            except AttributeError:
                                pass
                            print("Info type: {}".format(finding.info_type.name))
                            # Convert likelihood value to string respresentation.
                            likelihood = finding.likelihood.name
                            print("Likelihood: {}".format(likelihood))
                            if likelihood in ['LIKELY', 'VERY_LIKELY']:
                                dado_encriptado = encrypt_symmetric(
                                    project_id = project_id,
                                    location_id = 'global',
                                    key_ring_id = 'teste',
                                    key_id = 'chave',
                                    plaintext = element
                                )
                                new_row.append(str(dado_encriptado)[2:-2])
                            else:
                                new_row.append(element)
                    else:
                        new_row.append(element)
                writer.writerow(new_row)