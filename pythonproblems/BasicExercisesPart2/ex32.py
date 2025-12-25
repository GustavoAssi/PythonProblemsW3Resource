from pythonproblems.functions.utils import Input


def top_three_building_heights() -> None:
    """
    This program finds the heights of the top three buildings 
    in descending order from eight given buildings.
    Author: Gustavo Assi Alencar.
    Date:   23/12/2025.
    """

    # Step 1: Get the height of the builds.
    building_heights = []
    for index in range(8):
        building_name = Input.get_string(f"Type the name of {index + 1}º building: ", stripped=True)
        building_height = Input.get_float_number(f"Type the {index + 1}º building height (in meters): ", must_be_positive=True)
        building_info = {"building name": building_name, "building height": building_height}
        building_heights.append(building_info)

    # Step 2: Sort the hights in descending order.
    heights_rank = sorted(building_heights, key=lambda building: building["building height"], reverse=True)

    # Step 3: Display top three building hights.
    print("\n")
    for index in range(3):
        print(f">>> {index + 1}º place: {heights_rank[index]["building name"]}, with {heights_rank[index]["building height"]} meters.")


def main() -> None:
    top_three_building_heights()


if __name__ == "__main__":
    main()
